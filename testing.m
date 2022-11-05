%% ve60 it=160ms                     0.150mA
% sat @ 640ms, blue light, blue channel

s60R320=x320ve60R./mean(x320ve60R(:,1));
s60G320=x320ve60G./mean(x320ve60G(:,2));
s60B320=x320ve60B./mean(x320ve60B(:,3));
s60C320=x320ve60C./mean(x320ve60C(:,4));

p60R320=x320ve60R(:,1)/192;
p60G320=x320ve60G(:,2)/148;
p60B320=x320ve60B(:,3)/112;

%% ice2

s60a40=x40ve60a./mean(x40ve60a);
s60t40=x40ve60t./mean(x40ve60a);
s60i40=x40ve60i./mean(x40ve60a);

%% ice2 fig

figure()
hold on
boxplot([s60i40(:,1), s60t40(:,1), s60a40(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60i40(:,2), s60t40(:,2), s60a40(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60i40(:,3), s60t40(:,3), s60a40(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60i40(:,4), s60t40(:,4), s60a40(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('VEML6040 First Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% ice3

s60A40=x40ve60A./mean(x40ve60A);
s60T40=x40ve60T./mean(x40ve60A);
s60I40=x40ve60I./mean(x40ve60A);

%% ice3 fig

figure()
hold on
boxplot([s60I40(:,1), s60T40(:,1), s60A40(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60I40(:,2), s60T40(:,2), s60A40(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60I40(:,3), s60T40(:,3), s60A40(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s60I40(:,4), s60T40(:,4), s60A40(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('VEML6040 Second Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% ve33 g=1x it=100ms                0.620mA
% sat @ 400ms, blue light, clear channel

s33R200=x200ve33R./mean(x200ve33R(:,1));
s33G200=x200ve33G./mean(x200ve33G(:,2));
s33B200=x200ve33B./mean(x200ve33B(:,3));
s33C200=x200ve33C./mean(x200ve33C(:,4));

p33R200=x200ve33R(:,1)/82;
p33G200=x200ve33G(:,2)/78;
p33B200=x200ve33B(:,3)/68;

%boxplot([s33R200, s33G200, s33B200, s33C200], 'Labels',{'Red','Green','Blue','Clear'})

%% ice2

s33a50=x50ve33a./mean(x50ve33a);
s33t50=x50ve33t./mean(x50ve33a);
s33i50=x50ve33i./mean(x50ve33a);

%p33a50=x50ve33a./mean(x50ve33a);
%p33t50=x50ve33t./mean(x50ve33a);
%p33i50=x50ve33i./mean(x50ve33a);

%% ice2 fig

figure()
hold on
boxplot([s33i50(:,1), s33t50(:,1), s33a50(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33i50(:,2), s33t50(:,2), s33a50(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33i50(:,3), s33t50(:,3), s33a50(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33i50(:,4), s33t50(:,4), s33a50(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('VEML3328 First Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')
xlim([0 1.22])

%% ice2 fig v2

%figure()
%hold on
%boxchart([s33i50(:,1), s33t50(:,1), s33a50(:,1)], 'BoxFaceColor','r')
%boxchart([s33i50(:,2), s33t50(:,2), s33a50(:,2)], 'BoxFaceColor','g')
%boxchart([s33i50(:,3), s33t50(:,3), s33a50(:,3)], 'BoxFaceColor','b')
%boxchart([s33i50(:,4), s33t50(:,4), s33a50(:,4)], 'BoxFaceColor','k')
%boxplot([s33i50(:,2), s33t50(:,2), s33a50(:,2)], 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
%boxplot([s33i50(:,3), s33t50(:,3), s33a50(:,3)], 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
%boxplot([s33i50(:,4), s33t50(:,4), s33a50(:,4)], 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
%view([90 -90])
%% ice3

s33A50=x50ve33A./mean(x50ve33A);
s33T50=x50ve33T./mean(x50ve33A);
s33I50=x50ve33I./mean(x50ve33A);

%% ice3 fig

figure()
hold on
boxplot([s33I50(:,1), s33T50(:,1), s33A50(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33I50(:,2), s33T50(:,2), s33A50(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33I50(:,3), s33T50(:,3), s33A50(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([s33I50(:,4), s33T50(:,4), s33A50(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('VEML3328 Second Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')
xlim([0 1.05])

%% tcs g=16x it=24ms                0.320mA    0.550mA
% no saturation

stcs5R700=x700tcs5R./mean(x700tcs5R(:,1));
stcs5G700=x700tcs5G./mean(x700tcs5G(:,2));
stcs5B700=x700tcs5B./mean(x700tcs5B(:,3));
stcs5C700=x700tcs5C./mean(x700tcs5C(:,4));

ptcs5R700=x700tcs5R(:,1)/(.95*19.5*1.6);
ptcs5G700=x700tcs5G(:,2)/(.725*16.6*1.6);
ptcs5B700=x700tcs5B(:,3)/(.765*13.8*1.6);

%% ice2

stcsa101=x101tcs5a./mean(x101tcs5a);
stcst101=x101tcs5t./mean(x101tcs5a);
stcsi101=x101tcs5i./mean(x101tcs5a);

%% ice2 fig

figure()
hold on
boxplot([stcsi101(:,1), stcst101(:,1), stcsa101(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsi101(:,2), stcst101(:,2), stcsa101(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsi101(:,3), stcst101(:,3), stcsa101(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsi101(:,4), stcst101(:,4), stcsa101(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('TCS34725 First Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% ice3

stcsA101=x101tcs5A./mean(x101tcs5A);
stcsT101=x101tcs5T./mean(x101tcs5A);
stcsI101=x101tcs5t./mean(x101tcs5A);

%% ice3 fig

figure()
hold on
boxplot([stcsI101(:,1), stcsT101(:,1), stcsA101(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsI101(:,2), stcsT101(:,2), stcsA101(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsI101(:,3), stcsT101(:,3), stcsA101(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([stcsI101(:,4), stcsT101(:,4), stcsA101(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('TCS34725 Second Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% bh g=16x it=160ms                 0.160mA
% no saturation

sbhR5120=x5120bhR./mean(x5120bhR(:,1));
sbhG5120=x5120bhG./mean(x5120bhG(:,2));
sbhB5120=x5120bhB./mean(x5120bhB(:,3));
sbhC5120=x5120bhC./mean(x5120bhC(:,4));

pbhR5120=x5120bhR(:,1)/(4000/10);
pbhG5120=x5120bhG(:,2)/(3350/10);
pbhB5120=x5120bhB(:,3)/(2370/10);

%% ice2

sbha160=x160bha./mean(x160bha);
sbht160=x160bht./mean(x160bha);
sbhi160=x160bhi./mean(x160bha);

%% ice2 fig

figure()
hold on
boxplot([sbhi160(:,1), sbht160(:,1), sbha160(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhi160(:,2), sbht160(:,2), sbha160(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhi160(:,3), sbht160(:,3), sbha160(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhi160(:,4), sbht160(:,4), sbha160(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('BH1745NUC First Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% ice3

sbhA160=x160bhA./mean(x160bhA);
sbhT160=x160bhT./mean(x160bhA);
sbhI160=x160bhI./mean(x160bhA);

%% ice3 fig

figure()
hold on
boxplot([sbhI160(:,1), sbhT160(:,1), sbhA160(:,1)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','r', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhI160(:,2), sbhT160(:,2), sbhA160(:,2)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','g', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhI160(:,3), sbhT160(:,3), sbhA160(:,3)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','b', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
boxplot([sbhI160(:,4), sbhT160(:,4), sbhA160(:,4)], 'Orientation','horizontal', 'MedianStyle','target', 'Symbol', 'x', 'Colors','k', 'Widths',0.2, 'Labels',{'Ice','Container','Ambient'})
hold off
title('BH1745NUC Second Ice Test Normalised Response')
xlabel('Response Normalised to Ambient Response')
ylabel('Conditions')

%% irrad fig

figure()
hold on
boxplot([p33R200, p33G200, p33B200], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue'})
boxplot([p60R320, p60G320, p60B320], 'Symbol', 'x', 'Colors','g', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue'})
boxplot([ptcs5R700, ptcs5G700, ptcs5B700], 'Symbol', 'x', 'Colors','k', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue'})
boxplot([pbhR5120, pbhG5120, pbhB5120], 'Symbol', 'x', 'Colors','r', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue'})
hold off
title('Measured Irradiance Per Channel')
xlabel('Channel')
ylabel('Irradiance (μW/cm^2)')

%% rel to c

figure()
hold on
boxplot([s33C200(:,1), s33C200(:,2), s33C200(:,3), s33C200(:,4)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([s60C320(:,1), s60C320(:,2), s60C320(:,3), s60C320(:,4)], 'Symbol', 'x', 'Colors','g', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([stcs5C700(:,1), stcs5C700(:,2), stcs5C700(:,3), stcs5C700(:,4)], 'Symbol', 'x', 'Colors','k', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([sbhC5120(:,1), sbhC5120(:,2), sbhC5120(:,3), sbhC5120(:,4)], 'Symbol', 'x', 'Colors','r', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
hold off
title('Channel Responsivity Relative to Clear Channel')
xlabel('Channel')
ylabel('Normalised Response')

%%

figure()
hold on
boxplot([s33R200(:,1), s33R200(:,2), s33R200(:,3), s33R200(:,4)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([s60R320(:,1), s60R320(:,2), s60R320(:,3), s60R320(:,4)], 'Symbol', 'x', 'Colors','g', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([stcs5R700(:,1), stcs5R700(:,2), stcs5R700(:,3), stcs5R700(:,4)], 'Symbol', 'x', 'Colors','k', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([sbhR5120(:,1), sbhR5120(:,2), sbhR5120(:,3), sbhR5120(:,4)], 'Symbol', 'x', 'Colors','r', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
hold off
title('Channel Responsivity Relative to Red Channel')
xlabel('Channel')
ylabel('Normalised Response')
 
figure()
hold on
boxplot([s33G200(:,1), s33G200(:,2), s33G200(:,3), s33G200(:,4)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([s60G320(:,1), s60G320(:,2), s60G320(:,3), s60G320(:,4)], 'Symbol', 'x', 'Colors','g', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([stcs5G700(:,1), stcs5G700(:,2), stcs5G700(:,3), stcs5G700(:,4)], 'Symbol', 'x', 'Colors','k', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([sbhG5120(:,1), sbhG5120(:,2), sbhG5120(:,3), sbhG5120(:,4)], 'Symbol', 'x', 'Colors','r', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
hold off
title('Channel Responsivity Relative to Green Channel')
xlabel('Channel')
ylabel('Normalised Response')

figure()
hold on
boxplot([s33B200(:,1), s33B200(:,2), s33B200(:,3), s33B200(:,4)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([s60B320(:,1), s60B320(:,2), s60B320(:,3), s60B320(:,4)], 'Symbol', 'x', 'Colors','g', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([stcs5B700(:,1), stcs5B700(:,2), stcs5B700(:,3), stcs5B700(:,4)], 'Symbol', 'x', 'Colors','k', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
boxplot([sbhB5120(:,1), sbhB5120(:,2), sbhB5120(:,3), sbhB5120(:,4)], 'Symbol', 'x', 'Colors','r', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'Red','Green','Blue','Clear'})
hold off
title('Channel Responsivity Relative to Blue Channel')
xlabel('Channel')
ylabel('Normalised Response')

%% IT scaling

figure()
boxplot([x40ve60B(:,3), x80ve60B(:,3), x160ve60B(:,3), x320ve60B(:,3), x640ve60B(:,3), x1280ve60B(:,3)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'40','80','160','320','640','1280'})
%title('VEML6040 Blue Channel Response to Blue LED')
xlabel('Integration Time (ms)')
ylabel('Counts')

figure()
boxplot([x50ve33B(:,4), x100ve33B(:,4), x200ve33B(:,4), x400ve33B(:,4)], 'Symbol', 'x', 'MedianStyle','target', 'Widths',0.2, 'Labels',{'50','100','200','400'})
%title('VEML3328 Clear Channel Response to Blue LED')
xlabel('Integration Time (ms)')
ylabel('Counts')

%%
mean(x50ve33B(:,4))
mean(x100ve33B(:,4))
mean(x200ve33B(:,4))
mean(x400ve33B(:,4))

%%

r = [2.91, 4.64, 3.58, 6.79];
g = [106.81, 83.71, 163.51, 99.43];
b = [464.54, 364.05, 731.25, 254.03];
mad(r)
std(r)
mad(g)
std(g)
mad(b)
std(b)


