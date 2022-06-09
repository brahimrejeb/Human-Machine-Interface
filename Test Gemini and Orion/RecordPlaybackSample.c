	/* Copyright (C) 2012-2017 Ultraleap Limited. All rights reserved.
 *
 * Use of this code is subject to the terms of the Ultraleap SDK agreement
 * available at https://central.leapmotion.com/agreements/SdkAgreement unless
 * Ultraleap has signed a separate license agreement with you or your
 * organisation.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "LeapC.h"
#include "ExampleConnection.h"

int64_t lastFrameID = 0; //The last frame received

int main(int argc, char** argv) {
  OpenConnection();
  while(!IsConnected)
    millisleep(100); //wait a bit to let the connection complete

  printf("Connected.\n");
  LEAP_DEVICE_INFO* deviceProps = GetDeviceProperties();
  if(deviceProps)
    printf("Using device %s.\n", deviceProps->serial);

  LEAP_RECORDING recordingHandle;
  LEAP_RECORDING_PARAMETERS params;

  //Open the recording for writing
  params.mode = eLeapRecordingFlags_Writing;
  eLeapRS result = LeapRecordingOpen(&recordingHandle, "leapRecording.lmt", params);
  if(LEAP_SUCCEEDED(result)){
    int frameCount = 0;
    while(frameCount < 2000){
      LEAP_TRACKING_EVENT *frame = GetFrame();
      if(frame && (frame->tracking_frame_id > lastFrameID)){
        lastFrameID = frame->tracking_frame_id;
        frameCount++;
        uint64_t dataWritten = 0;
        result = LeapRecordingWrite(recordingHandle, frame, &dataWritten);
        printf("Recorded %"PRIu64" bytes for frame %"PRIu64" with %i hands.\n", dataWritten, frame->tracking_frame_id, frame->nHands);
      }
    }
    result = LeapRecordingClose(&recordingHandle);
    if(!LEAP_SUCCEEDED(result))
      printf("Failed to close recording: %s\n", ResultString(result));

    //Reopen the recording for reading
    char *filename = "test.txt";
    // open the file for writing
    FILE *fptr;

    // use appropriate location if you are using MacOS or Linux
    
    fptr = fopen(filename,"w");
    if(fptr == NULL)
    {
      printf("Error!");   
      exit(1);             
    }
    int y = -35;
    // fprintf(fptr,"%d", y);
    

    params.mode = eLeapRecordingFlags_Reading;
    result = LeapRecordingOpen(&recordingHandle, "leapRecording.lmt", params);
    if(LEAP_SUCCEEDED(result)){
      LEAP_TRACKING_EVENT *frame = 0;
      while(frameCount-- > 0){
        uint64_t nextFrameSize = 0;
        result = LeapRecordingReadSize(recordingHandle, &nextFrameSize);
        if(!LEAP_SUCCEEDED(result))
          printf("Couldn't get next frame size: %s\n", ResultString(result));
        if(nextFrameSize > 0){
          frame = (LEAP_TRACKING_EVENT *)malloc((size_t)nextFrameSize);
          result = LeapRecordingRead(recordingHandle, frame, nextFrameSize);
          if(LEAP_SUCCEEDED(result)){
            printf("Read frame %"PRIu64" with %i hands.\n", frame->tracking_frame_id, frame->nHands);
	        // fprintf(fptr,"with %i hands.\n", frame->nHands);
            for (uint32_t h = 0; h < frame->nHands; h++) {
                LEAP_HAND * hand = &frame->pHands[h];
            
                for (int f = 0; f < 5; f++) {
                    LEAP_DIGIT finger = hand->digits[f];
                    for (int b = 0; b < 4; b++) {
                        LEAP_BONE bone = finger.bones[b];
                        printf("Hand id %i is a %s hand with position (%f, %f, %f).\n",hand->id,
                                   (hand->type == eLeapHandType_Left ? "left" : "right"),
                                    bone.prev_joint.x,
                                    bone.prev_joint.y,
                                    bone.prev_joint.z);
                        if (f < 4 || b<3) {
                            if (b<3){
                            fprintf(fptr, "%f,%f,%f,", bone.prev_joint.x, bone.prev_joint.y, bone.prev_joint.z);
                            }
                            else {
                                fprintf(fptr, "%f,%f,%f,", bone.next_joint.x, bone.next_joint.y, bone.next_joint.z);
                            }
                        }
                        else {
                            fprintf(fptr, "%f,%f,%f \n", bone.next_joint.x, bone.next_joint.y, bone.next_joint.z);
                        }

                        
                    }
                }
            }
          } else {
            printf("Could not read frame: %s\n", ResultString(result));
          }
        }
      }
      fclose(fptr);
      return 0;
      result = LeapRecordingClose(&recordingHandle);
      if(!LEAP_SUCCEEDED(result))
        printf("Failed to close recording: %s\n", ResultString(result));
    } else {
      printf("Failed to open recording for reading: %s\n", ResultString(result));
    }
  } else {
    printf("Failed to open recording for writing: %s\n", ResultString(result));
  }

}
//End-of-Sample
