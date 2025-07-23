# タスク: このCコードをVerilogに変換して
## Cコード:
```c
int16_t error = ref - meas;
int16_t output = (Kp * error + Ki * integral) >> 4;
```
