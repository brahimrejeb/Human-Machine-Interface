% The goal of this matlab file is to analyze the measure obtain when we use
% the gemini software so that we can compare it with the measure taken
% using the orion software. 

%% 
clear all;
close all; 

%%
 A=readmatrix('measure_gemini.txt');

% thumb angle : 
thumb2=[A(:,4),A(:,5),A(:,6)]-[A(:,7),A(:,8),A(:,9)];
thumb1=[A(:,10),A(:,11),A(:,12)]-[A(:,7),A(:,8),A(:,9)];

for i=1:length(A)
    thumb_angle(i) = atan2(norm(cross(thumb1(i,:),thumb2(i,:))),dot(thumb1(i,:),thumb2(i,:)));
end
      
% index angle :
index2=[A(:,13),A(:,14),A(:,15)]-[A(:,16),A(:,17),A(:,18)];
index1=[A(:,22),A(:,23),A(:,24)]-[A(:,16),A(:,17),A(:,18)];

for i=1:length(A)
    index_angle(i) = atan2(norm(cross(index1(i,:),index2(i,:))),dot(index1(i,:),index2(i,:)));
end
  
% middle angle
middle2=[A(:,25),A(:,26),A(:,27)]-[A(:,28),A(:,29),A(:,30)];
middle1=[A(:,34),A(:,35),A(:,36)]-[A(:,28),A(:,29),A(:,30)];

for i=1:length(A)
    middle_angle(i) = atan2(norm(cross(middle1(i,:),middle2(i,:))),dot(middle1(i,:),middle2(i,:)));
end

   
% ring angle
ring2=[A(:,37),A(:,38),A(:,39)]-[A(:,40),A(:,41),A(:,42)];
ring1=[A(:,46),A(:,47),A(:,48)]-[A(:,40),A(:,41),A(:,42)];

for i=1:length(A)
    ring_angle(i) = atan2(norm(cross(ring1(i,:),ring2(i,:))),dot(ring1(i,:),ring2(i,:)));
end

% pinky angle
pinky2=[A(:,49),A(:,50),A(:,51)]-[A(:,52),A(:,53),A(:,54)];
pinky1=[A(:,58),A(:,59),A(:,60)]-[A(:,52),A(:,53),A(:,54)];

for i=1:length(A)
    pinky_angle(i) = atan2(norm(cross(pinky1(i,:),pinky2(i,:))),dot(pinky1(i,:),pinky2(i,:)));
end
    

t=[1:length(A)];

%% Plot for meta_angle (distance between other finger and thumb) : 
ymax=max([thumb_angle,index_angle,middle_angle,ring_angle,pinky_angle],[],'all');
ymin=min([thumb_angle,index_angle,middle_angle,ring_angle,pinky_angle],[],'all');

f = figure;

subplot(5,1,1);
plot(t,thumb_angle)
set(gca,'ylim',[ymin ymax])
legend('thumb')

subplot(5,1,2);
plot(t,index_angle)
set(gca,'ylim',[ymin ymax])
legend('index')

subplot(5,1,3);
plot(t,middle_angle)
set(gca,'ylim',[ymin ymax])
legend('mddle\_finger')


subplot(5,1,4);
plot(t,ring_angle)
set(gca,'ylim',[ymin ymax])
legend('ring')


subplot(5,1,5);
plot(t,pinky_angle)
set(gca,'ylim',[ymin ymax])
legend('pinky')

a = axes;
t1 = title('finger angle meta-distal');
a.Visible = 'off';
t1.Visible = 'on';
