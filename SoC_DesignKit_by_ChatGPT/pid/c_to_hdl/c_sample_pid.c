// c_sample_pid.c
// PID制御ループ（固定小数点風）

int16_t error = ref - meas;
int16_t output = (Kp * error + Ki * integral) >> 4;
