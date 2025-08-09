%% Digital H∞ Control Design Example
% Author: Shinichi Samizo
% Description:
%   Continuous-time H∞ design -> Discretization -> Step & Bode evaluation

clear; clc;

%% 1. Plant model (example: 2nd-order system)
A = [0 1; -100 -20];
B = [0; 100];
C = [1 0];
D = 0;
P = ss(A,B,C,D);

%% 2. Weighting functions
s = tf('s');
W1 = (s/10 + 1)/(s/100 + 1);   % Performance weight
W2 = (s/100 + 1)/(s/1000 + 1); % Control weight
Paug = augw(P, W1, W2);

%% 3. H∞ synthesis
nmeas = 1; ncon = 1;
[K,CL,gamma] = hinfsyn(Paug, nmeas, ncon);
disp("H∞ gamma = " + gamma);

%% 4. Continuous response (singular values)
figure;
sigma(CL); grid on; title('Continuous-time H∞ Closed-loop Singular Values');

%% 5. Discretization
Ts = 0.001; % 1 ms sampling
Kd = c2d(K, Ts, 'tustin');

%% 6. Step response comparison
Gcl_cont = feedback(P*K, 1);
Gcl_disc = c2d(Gcl_cont, Ts, 'tustin');

figure;
step(Gcl_cont, 'b', Gcl_disc, 'r--');
legend('Continuous', 'Discrete', 'Location','best');
title('Step Response: Continuous vs Digital H∞');
grid on;

%% Ensure figures directory exists (run from simulation/)
figdir = fullfile('..','figures');
if ~exist(figdir, 'dir'); mkdir(figdir); end

%% Save step response figure
print('-dpng', fullfile(figdir, 'digital_hinf_step.png'));

%% 7. Bode plot: Continuous vs Digital H∞ (saved)
figure;
bode(Gcl_disc, 'r', Gcl_cont, 'b--');
legend('Discrete', 'Continuous', 'Location','best');
title('Bode Plot: Continuous vs Digital H∞');
grid on;
print('-dpng', fullfile(figdir, 'digital_hinf_bode.png'));

% (optional) close figures after saving
% close all
