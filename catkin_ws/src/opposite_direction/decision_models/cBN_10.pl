%%%%%%%%%%%%%%%%%%%%%%%%%%
% Probabilistic facts
%%%%%%%%%%%%%%%%%%%%%%%%%%

0.5229874::u1.
curr_lane :- u1.
0.6863702::u2.
free_E :- u2.
0.4505536::u3.
free_NE :- u3.
0.3383374::u4.
free_NW :- u4.
0.5998624::u5.
free_SE :- u5.
0.70157::u6.
free_SW :- u6.
0.7325952::u7.
free_W :- u7.


%%%%%%%%%%%%%%%%%%%%%%%%%%
% Rules
%%%%%%%%%%%%%%%%%%%%%%%%%%


0.378611::action(change_to_left); 0.2650277::action(change_to_right); 0.3533703::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.3323363::action(change_to_left); 0.3722167::action(change_to_right); 0.292456::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.9950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.3437962::action(change_to_left); 0.360986::action(change_to_right); 0.2922268::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.0009960159::action(change_to_left); 0.4169369::action(change_to_right); 0.579079::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.4763554::action(change_to_left); 0.0009960159::action(change_to_right); 0.5196605::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.424652::action(change_to_left); 0.5538939::action(change_to_right); 0.01846313::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.569152::action(change_to_left); 0.426864::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.498008::action(change_to_left); 0.498008::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.5090748::action(change_to_left); 0.4869411::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.3486056::action(change_to_left); 0.6474104::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.498008::action(change_to_left); 0.0009960159::action(change_to_right); 0.498008::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, \+ free_W. 


0.3612351::action(change_to_left); 0.3612351::action(change_to_right); 0.2745387::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.340103::action(change_to_left); 0.0009960159::action(change_to_right); 0.6559129::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.3958712::action(change_to_left); 0.2932379::action(change_to_right); 0.3078998::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.1410354::action(change_to_left); 0.2938238::action(change_to_right); 0.2115532::action(cruise); 0.3408356::action(keep); 0.000999001::action(swerve_left); 0.01175295::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.2623708::action(change_to_left); 0.4066747::action(change_to_right); 0.3279635::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.5844535::action(change_to_left); 0.01718981::action(change_to_right); 0.3953656::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.1125655::action(change_to_left); 0.06753932::action(change_to_right); 0.8169041::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.2731531::action(change_to_left); 0.3824144::action(change_to_right); 0.3414414::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.579079::action(change_to_left); 0.4169369::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.000997009::action(change_to_left); 0.2524073::action(change_to_right); 0.4669536::action(cruise); 0.2776481::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.6010441::action(change_to_left); 0.3949718::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, free_SE, \+ free_SW, \+ free_W. 


0.3195542::action(change_to_left); 0.3323363::action(change_to_right); 0.3451185::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.471797::action(change_to_left); 0.0009960159::action(change_to_right); 0.5242189::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.1603935::action(change_to_left); 0.130691::action(change_to_right); 0.2079175::action(cruise); 0.499002::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.2706167::action(change_to_left); 0.2991027::action(change_to_right); 0.4272896::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.5164527::action(change_to_left); 0.0009960159::action(change_to_right); 0.4795632::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.2729906::action(change_to_left); 0.3916821::action(change_to_right); 0.3323363::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, \+ free_W. 


0.4300978::action(change_to_left); 0.5659181::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.9950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.000997009::action(change_to_left); 0.2387205::action(change_to_right); 0.3791443::action(cruise); 0.3791443::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.4569624::action(change_to_left); 0.3531073::action(change_to_right); 0.1869392::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, \+ free_SE, free_SW, \+ free_W. 


0.3195542::action(change_to_left); 0.3451185::action(change_to_right); 0.3323363::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.3798129::action(change_to_left); 0.3481619::action(change_to_right); 0.000997009::action(cruise); 0.2690342::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.4368916::action(change_to_left); 0.3360704::action(change_to_right); 0.224047::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.07739623::action(change_to_left); 0.1018371::action(change_to_right); 0.1588659::action(cruise); 0.6599047::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.0009960159::action(change_to_left); 0.5922257::action(change_to_right); 0.4037902::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.3363404::action(change_to_left); 0.3964012::action(change_to_right); 0.2642674::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.0009960159::action(change_to_left); 0.0009960159::action(change_to_right); 0.992864::action(cruise); 0.003151949::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, free_SE, free_SW, \+ free_W. 


0.5101545::action(change_to_left); 0.4858614::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.287097::action(change_to_left); 0.3964673::action(change_to_right); 0.3007683::action(cruise); 0.01367129::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.5666987::action(change_to_left); 0.4293172::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.3776549::action(change_to_left); 0.4531859::action(change_to_right); 0.1661682::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.0719491::action(change_to_left); 0.08736677::action(change_to_right); 0.8376931::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, free_SE, free_SW, \+ free_W. 


0.4197933::action(change_to_left); 0.5072502::action(change_to_right); 0.000997009::action(cruise); 0.06996554::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.498008::action(change_to_left); 0.498008::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.3057494::action(change_to_left); 0.2525756::action(change_to_right); 0.4386839::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.3584751::action(change_to_left); 0.3472728::action(change_to_right); 0.291261::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.000997009::action(change_to_left); 0.4615782::action(change_to_right); 0.4985045::action(cruise); 0.03692626::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.6941929::action(change_to_left); 0.0009960159::action(change_to_right); 0.301823::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, \+ free_SW, free_W. 


0.2769469::action(change_to_left); 0.4015731::action(change_to_right); 0.318489::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.0009950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.9950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.3962472::action(change_to_left); 0.3579007::action(change_to_right); 0.2428612::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.9950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.01994018::action(change_to_left); 0.4187438::action(change_to_right); 0.558325::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, \+ free_SE, \+ free_SW, free_W. 


0.0009960159::action(change_to_left); 0.0009960159::action(change_to_right); 0.8674978::action(cruise); 0.1285182::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.230079::action(change_to_left); 0.4090293::action(change_to_right); 0.3579007::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.4864264::action(change_to_left); 0.0009960159::action(change_to_right); 0.5095895::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.000997009::action(change_to_left); 0.2291975::action(change_to_right); 0.3552561::action(cruise); 0.4125554::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.5206447::action(change_to_left); 0.4753712::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.1666667::action(change_to_left); 0.1666667::action(change_to_right); 0.1666667::action(cruise); 0.1666667::action(keep); 0.1666667::action(swerve_left); 0.1666667::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.0181068::action(change_to_left); 0.02236722::action(change_to_right); 0.9564649::action(cruise); 0.001065106::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, free_SE, \+ free_SW, free_W. 


0.2286718::action(change_to_left); 0.2012312::action(change_to_right); 0.567106::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.0009950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.9950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.1949459::action(change_to_left); 0.1169675::action(change_to_right); 0.6850956::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.6181456::action(change_to_left); 0.000997009::action(change_to_right); 0.1196411::action(cruise); 0.2592223::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.0009960159::action(change_to_left); 0.7636122::action(change_to_right); 0.2324037::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.9577076::action(change_to_left); 0.0009960159::action(change_to_right); 0.03830831::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.1034957::action(change_to_left); 0.03967337::action(change_to_right); 0.8538399::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, free_SE, \+ free_SW, free_W. 


0.0009960159::action(change_to_left); 0.0009960159::action(change_to_right); 0.06574824::action(cruise); 0.9302677::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.2982541::action(change_to_left); 0.3441393::action(change_to_right); 0.2982541::action(cruise); 0.05735655::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.01874854::action(change_to_left); 0.0009960159::action(change_to_right); 0.0009960159::action(cruise); 0.9772674::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.1175182::action(change_to_left); 0.000997009::action(change_to_right); 0.06444545::action(cruise); 0.8150454::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.0891893::action(change_to_left); 0.000997009::action(change_to_right); 0.1083013::action(cruise); 0.7995184::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.0009960159::action(change_to_left); 0.5174109::action(change_to_right); 0.4786051::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.0009960159::action(change_to_left); 0.1124112::action(change_to_right); 0.8836047::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, \+ free_SE, free_SW, free_W. 


0.0009950249::action(change_to_left); 0.0009950249::action(change_to_right); 0.9950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.0009960159::action(change_to_left); 0.471797::action(change_to_right); 0.5242189::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.000997009::action(change_to_left); 0.1688483::action(change_to_right); 0.8201203::action(cruise); 0.000997009::action(keep); 0.008040395::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.01513638::action(change_to_left); 0.4995005::action(change_to_right); 0.3935458::action(cruise); 0.07568189::action(keep); 0.01513638::action(swerve_left); 0.000999001::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.08669643::action(change_to_left); 0.1114668::action(change_to_right); 0.7988457::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.05247416::action(change_to_left); 0.8920607::action(change_to_right); 0.05247416::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.06662314::action(change_to_left); 0.9293928::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.0009950249::action(change_to_left); 0.9950249::action(change_to_right); 0.0009950249::action(cruise); 0.0009950249::action(keep); 0.0009950249::action(swerve_left); 0.0009950249::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, \+ free_SE, free_SW, free_W. 


0.07653405::action(change_to_left); 0.05816588::action(change_to_right); 0.1224545::action(cruise); 0.7408496::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.1009218::action(change_to_left); 0.119611::action(change_to_right); 0.1009218::action(cruise); 0.6765495::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.02894763::action(change_to_left); 0.04411067::action(change_to_right); 0.04686759::action(cruise); 0.8780781::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.03441169::action(change_to_left); 0.000997009::action(change_to_right); 0.03999196::action(cruise); 0.9226053::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.1846019::action(change_to_left); 0.1326826::action(change_to_right); 0.1730643::action(cruise); 0.5076552::action(keep); 0.000998004::action(swerve_left); 0.000998004::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.2195249::action(change_to_left); 0.3292874::action(change_to_right); 0.4481967::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.3713958::action(change_to_left); 0.0009960159::action(change_to_right); 0.6246202::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.0009960159::action(change_to_left); 0.06479658::action(change_to_right); 0.9312194::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- curr_lane, free_E, free_NE, \+ free_NW, free_SE, free_SW, free_W. 


0.969805::action(change_to_left); 0.0009960159::action(change_to_right); 0.0009960159::action(cruise); 0.02621095::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, free_SW, free_W. 


0.760384::action(change_to_left); 0.000998004::action(change_to_right); 0.201977::action(cruise); 0.023762::action(keep); 0.011881::action(swerve_left); 0.000998004::action(swerve_right) :- curr_lane, \+ free_E, \+ free_NE, free_NW, free_SE, free_SW, free_W. 


0.0009960159::action(change_to_left); 0.0009960159::action(change_to_right); 0.9872533::action(cruise); 0.008762604::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, free_E, \+ free_NE, free_NW, free_SE, free_SW, free_W. 


0.4698548::action(change_to_left); 0.000997009::action(change_to_right); 0.3437962::action(cruise); 0.183358::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, free_E, \+ free_NE, free_NW, free_SE, free_SW, free_W. 


0.4889533::action(change_to_left); 0.5070627::action(change_to_right); 0.0009960159::action(cruise); 0.0009960159::action(keep); 0.0009960159::action(swerve_left); 0.0009960159::action(swerve_right) :- \+ curr_lane, \+ free_E, free_NE, free_NW, free_SE, free_SW, free_W. 


0.6580259::action(change_to_left); 0.2691924::action(change_to_right); 0.06979063::action(cruise); 0.000997009::action(keep); 0.000997009::action(swerve_left); 0.000997009::action(swerve_right) :- curr_lane, \+ free_E, free_NE, free_NW, free_SE, free_SW, free_W. 


0.0551173::action(change_to_left); 0.07578628::action(change_to_right); 0.8520215::action(cruise); 0.009186216::action(keep); 0.006889662::action(swerve_left); 0.000999001::action(swerve_right) :- \+ curr_lane, free_E, free_NE, free_NW, free_SE, free_SW, free_W. 


0.5080748::action(change_to_left); 0.000998004::action(change_to_right); 0.000998004::action(cruise); 0.09072764::action(keep); 0.2994012::action(swerve_left); 0.0998004::action(swerve_right) :- curr_lane, free_E, free_NE, free_NW, free_SE, free_SW, free_W. 


0.999001::u8.
latent_collision :- action(change_to_left), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u8. 


0.999001::u9.
latent_collision :- action(change_to_right), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u9. 


0.999001::u10.
latent_collision :- action(cruise), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u10. 


0.5::u11.
latent_collision :- action(keep), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u11. 


0.5::u12.
latent_collision :- action(swerve_left), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u12. 


0.5::u13.
latent_collision :- action(swerve_right), \+ curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u13. 


0.999001::u14.
latent_collision :- action(change_to_left), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u14. 


0.999001::u15.
latent_collision :- action(change_to_right), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u15. 


0.999001::u16.
latent_collision :- action(cruise), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u16. 


0.000999001::u17.
latent_collision :- action(keep), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u17. 


0.5::u18.
latent_collision :- action(swerve_left), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u18. 


0.000999001::u19.
latent_collision :- action(swerve_right), curr_lane, \+ free_NE, \+ free_NW, \+ free_W, u19. 


0.999001::u20.
latent_collision :- action(change_to_left), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u20. 


0.9892473::u21.
latent_collision :- action(change_to_right), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u21. 


0.999001::u22.
latent_collision :- action(cruise), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u22. 


0.5::u23.
latent_collision :- action(keep), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u23. 


0.5::u24.
latent_collision :- action(swerve_left), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u24. 


0.5::u25.
latent_collision :- action(swerve_right), \+ curr_lane, free_NE, \+ free_NW, \+ free_W, u25. 


0.999001::u26.
latent_collision :- action(change_to_left), curr_lane, free_NE, \+ free_NW, \+ free_W, u26. 


0.999001::u27.
latent_collision :- action(change_to_right), curr_lane, free_NE, \+ free_NW, \+ free_W, u27. 


0.000999001::u28.
latent_collision :- action(cruise), curr_lane, free_NE, \+ free_NW, \+ free_W, u28. 


0.000999001::u29.
latent_collision :- action(keep), curr_lane, free_NE, \+ free_NW, \+ free_W, u29. 


0.5::u30.
latent_collision :- action(swerve_left), curr_lane, free_NE, \+ free_NW, \+ free_W, u30. 


0.5::u31.
latent_collision :- action(swerve_right), curr_lane, free_NE, \+ free_NW, \+ free_W, u31. 


0.999001::u32.
latent_collision :- action(change_to_left), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u32. 


0.999001::u33.
latent_collision :- action(change_to_right), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u33. 


0.5::u34.
latent_collision :- action(cruise), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u34. 


0.5::u35.
latent_collision :- action(keep), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u35. 


0.5::u36.
latent_collision :- action(swerve_left), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u36. 


0.5::u37.
latent_collision :- action(swerve_right), \+ curr_lane, \+ free_NE, free_NW, \+ free_W, u37. 


0.999001::u38.
latent_collision :- action(change_to_left), curr_lane, \+ free_NE, free_NW, \+ free_W, u38. 


0.999001::u39.
latent_collision :- action(change_to_right), curr_lane, \+ free_NE, free_NW, \+ free_W, u39. 


0.999001::u40.
latent_collision :- action(cruise), curr_lane, \+ free_NE, free_NW, \+ free_W, u40. 


0.000999001::u41.
latent_collision :- action(keep), curr_lane, \+ free_NE, free_NW, \+ free_W, u41. 


0.5::u42.
latent_collision :- action(swerve_left), curr_lane, \+ free_NE, free_NW, \+ free_W, u42. 


0.5::u43.
latent_collision :- action(swerve_right), curr_lane, \+ free_NE, free_NW, \+ free_W, u43. 


0.999001::u44.
latent_collision :- action(change_to_left), \+ curr_lane, free_NE, free_NW, \+ free_W, u44. 


0.999001::u45.
latent_collision :- action(change_to_right), \+ curr_lane, free_NE, free_NW, \+ free_W, u45. 


0.5::u46.
latent_collision :- action(cruise), \+ curr_lane, free_NE, free_NW, \+ free_W, u46. 


0.5::u47.
latent_collision :- action(keep), \+ curr_lane, free_NE, free_NW, \+ free_W, u47. 


0.5::u48.
latent_collision :- action(swerve_left), \+ curr_lane, free_NE, free_NW, \+ free_W, u48. 


0.5::u49.
latent_collision :- action(swerve_right), \+ curr_lane, free_NE, free_NW, \+ free_W, u49. 


0.999001::u50.
latent_collision :- action(change_to_left), curr_lane, free_NE, free_NW, \+ free_W, u50. 


0.999001::u51.
latent_collision :- action(change_to_right), curr_lane, free_NE, free_NW, \+ free_W, u51. 


0.000999001::u52.
latent_collision :- action(cruise), curr_lane, free_NE, free_NW, \+ free_W, u52. 


0.5::u53.
latent_collision :- action(keep), curr_lane, free_NE, free_NW, \+ free_W, u53. 


0.5::u54.
latent_collision :- action(swerve_left), curr_lane, free_NE, free_NW, \+ free_W, u54. 


0.5::u55.
latent_collision :- action(swerve_right), curr_lane, free_NE, free_NW, \+ free_W, u55. 


0.999001::u56.
latent_collision :- action(change_to_left), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u56. 


0.999001::u57.
latent_collision :- action(change_to_right), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u57. 


0.999001::u58.
latent_collision :- action(cruise), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u58. 


0.000999001::u59.
latent_collision :- action(keep), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u59. 


0.5::u60.
latent_collision :- action(swerve_left), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u60. 


0.5::u61.
latent_collision :- action(swerve_right), \+ curr_lane, \+ free_NE, \+ free_NW, free_W, u61. 


0.999001::u62.
latent_collision :- action(change_to_left), curr_lane, \+ free_NE, \+ free_NW, free_W, u62. 


0.999001::u63.
latent_collision :- action(change_to_right), curr_lane, \+ free_NE, \+ free_NW, free_W, u63. 


0.999001::u64.
latent_collision :- action(cruise), curr_lane, \+ free_NE, \+ free_NW, free_W, u64. 


0.000999001::u65.
latent_collision :- action(keep), curr_lane, \+ free_NE, \+ free_NW, free_W, u65. 


0.5::u66.
latent_collision :- action(swerve_left), curr_lane, \+ free_NE, \+ free_NW, free_W, u66. 


0.5::u67.
latent_collision :- action(swerve_right), curr_lane, \+ free_NE, \+ free_NW, free_W, u67. 


0.999001::u68.
latent_collision :- action(change_to_left), \+ curr_lane, free_NE, \+ free_NW, free_W, u68. 


0.5454545::u69.
latent_collision :- action(change_to_right), \+ curr_lane, free_NE, \+ free_NW, free_W, u69. 


0.999001::u70.
latent_collision :- action(cruise), \+ curr_lane, free_NE, \+ free_NW, free_W, u70. 


0.000999001::u71.
latent_collision :- action(keep), \+ curr_lane, free_NE, \+ free_NW, free_W, u71. 


0.5::u72.
latent_collision :- action(swerve_left), \+ curr_lane, free_NE, \+ free_NW, free_W, u72. 


0.5::u73.
latent_collision :- action(swerve_right), \+ curr_lane, free_NE, \+ free_NW, free_W, u73. 


0.999001::u74.
latent_collision :- action(change_to_left), curr_lane, free_NE, \+ free_NW, free_W, u74. 


0.999001::u75.
latent_collision :- action(change_to_right), curr_lane, free_NE, \+ free_NW, free_W, u75. 


0.000999001::u76.
latent_collision :- action(cruise), curr_lane, free_NE, \+ free_NW, free_W, u76. 


0.000999001::u77.
latent_collision :- action(keep), curr_lane, free_NE, \+ free_NW, free_W, u77. 


0.5::u78.
latent_collision :- action(swerve_left), curr_lane, free_NE, \+ free_NW, free_W, u78. 


0.5::u79.
latent_collision :- action(swerve_right), curr_lane, free_NE, \+ free_NW, free_W, u79. 


0.999001::u80.
latent_collision :- action(change_to_left), \+ curr_lane, \+ free_NE, free_NW, free_W, u80. 


0.999001::u81.
latent_collision :- action(change_to_right), \+ curr_lane, \+ free_NE, free_NW, free_W, u81. 


0.000999001::u82.
latent_collision :- action(cruise), \+ curr_lane, \+ free_NE, free_NW, free_W, u82. 


0.000999001::u83.
latent_collision :- action(keep), \+ curr_lane, \+ free_NE, free_NW, free_W, u83. 


0.000999001::u84.
latent_collision :- action(swerve_left), \+ curr_lane, \+ free_NE, free_NW, free_W, u84. 


0.5::u85.
latent_collision :- action(swerve_right), \+ curr_lane, \+ free_NE, free_NW, free_W, u85. 


0.000999001::u86.
latent_collision :- action(change_to_left), curr_lane, \+ free_NE, free_NW, free_W, u86. 


0.999001::u87.
latent_collision :- action(change_to_right), curr_lane, \+ free_NE, free_NW, free_W, u87. 


0.999001::u88.
latent_collision :- action(cruise), curr_lane, \+ free_NE, free_NW, free_W, u88. 


0.000999001::u89.
latent_collision :- action(keep), curr_lane, \+ free_NE, free_NW, free_W, u89. 


0.000999001::u90.
latent_collision :- action(swerve_left), curr_lane, \+ free_NE, free_NW, free_W, u90. 


0.5::u91.
latent_collision :- action(swerve_right), curr_lane, \+ free_NE, free_NW, free_W, u91. 


0.999001::u92.
latent_collision :- action(change_to_left), \+ curr_lane, free_NE, free_NW, free_W, u92. 


0.2658824::u93.
latent_collision :- action(change_to_right), \+ curr_lane, free_NE, free_NW, free_W, u93. 


0.000999001::u94.
latent_collision :- action(cruise), \+ curr_lane, free_NE, free_NW, free_W, u94. 


0.000999001::u95.
latent_collision :- action(keep), \+ curr_lane, free_NE, free_NW, free_W, u95. 


0.000999001::u96.
latent_collision :- action(swerve_left), \+ curr_lane, free_NE, free_NW, free_W, u96. 


0.5::u97.
latent_collision :- action(swerve_right), \+ curr_lane, free_NE, free_NW, free_W, u97. 


0.000999001::u98.
latent_collision :- action(change_to_left), curr_lane, free_NE, free_NW, free_W, u98. 


0.999001::u99.
latent_collision :- action(change_to_right), curr_lane, free_NE, free_NW, free_W, u99. 


0.000999001::u100.
latent_collision :- action(cruise), curr_lane, free_NE, free_NW, free_W, u100. 


0.000999001::u101.
latent_collision :- action(keep), curr_lane, free_NE, free_NW, free_W, u101. 


0.000999001::u102.
latent_collision :- action(swerve_left), curr_lane, free_NE, free_NW, free_W, u102. 


0.000999001::u103.
latent_collision :- action(swerve_right), curr_lane, free_NE, free_NW, free_W, u103. 


