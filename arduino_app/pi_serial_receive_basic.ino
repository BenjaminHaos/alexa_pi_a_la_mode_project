#include <IRremote.h>

// SONY A/V RECEIVER REMOTE CODES
unsigned long SONY_AV_RECV_POWER_STANDBY = 0x7620;
unsigned long SONY_AV_RECV_SELECT_INPUT_SAT_CATV = 0x600D;

// SAMSUNG TV REMOTE CODES
unsigned long SAMSUNG_TV_POWER_ON = 0xE0E09966;
unsigned long SAMSUNG_TV_POWER_OFF = 0xE0E019E6;

unsigned long SAMSUNG_TV_REMOTE_POWER_TOGGLE = 0xE0E040BF;
unsigned long SAMSUNG_TV_REMOTE_123_BUTTON = 0xE0E04BB4;
unsigned long SAMSUNG_TV_REMOTE_EXTRA_BUTTON =  0xE0E0738C;
unsigned long SAMSUNG_TV_REMOTE_UP_BOTTON =  0xE0E006F9;
unsigned long SAMSUNG_TV_REMOTE_LEFT_BUTTON =  0xE0E0A659;
unsigned long SAMSUNG_TV_REMOTE_RIGHT_BUTTON =  0xE0E046B9;
unsigned long SAMSUNG_TV_REMOTE_CENTER_BUTTON =  0xE0E016E9;
unsigned long SAMSUNG_TV_REMOTE_DOWN_BUTTON =  0xE0E08679;
unsigned long SAMSUNG_TV_REMOTE_BACK_BUTTON =  0xE0E01AE5;
unsigned long SAMSUNG_TV_REMOTE_HOME_BUTTON =  0xE0E09E61;
unsigned long SAMSUNG_TV_REMOTE_PLAY_PAUSE_BUTTON =  0xE0E09D62;
unsigned long SAMSUNG_TV_REMOTE_VOLUME_UP_BUTTON =  0xE0E0E01F;
unsigned long SAMSUNG_TV_REMOTE_VOLUME_DOWN_BUTTON =  0xE0E0D02F;
unsigned long SAMSUNG_TV_REMOTE_VOLUME_PRESS_BUTTON =  0xE0E0F00F;
unsigned long SAMSUNG_TV_REMOTE_CHANNEL_UP_BUTTON =  0xE0E048B7;
unsigned long SAMSUNG_TV_REMOTE_CHANNEL_DOWN_BUTTON =  0xE0E008F7;
unsigned long SAMSUNG_TV_REMOTE_CHANNEL_PRESS_BUTTON =  0xE0E0F20D;

//unsigned long MASTER_VOLUME_UP = 0x240C; // 15
//unsigned long MASTER_VOLUME_DOWN = 0x640C; // 15

IRsend irsend;

// ir_send pin is hard-coded in library to pin 3 on uno.

const int status_led_pin = 12;

int pi_code_received;

void light_status_light(int n)
{
	for (int i = 0; i < n; i++)
	{
		digitalWrite(status_led_pin, HIGH);
		delay(200);
		digitalWrite(status_led_pin, LOW);
		delay(100);
	}
}


void decode_serial_from_pi(int code_from_pi_to_decode)
{
	switch (code_from_pi_to_decode)
	{
		
		case 1:  // Samsung TV on.
			send_samsung_ir_signal(SAMSUNG_TV_POWER_ON, 32);
		break;
		
		case 2:  // Samsung TV off.
			send_samsung_ir_signal(SAMSUNG_TV_POWER_OFF, 32);
		break;

		case 3:	// Sony A/V Reciever on.
			send_sony_ir_signal(SONY_AV_RECV_SELECT_INPUT_SAT_CATV, 15);
		break;
		
		case 4:	// Sony A/V Reciever off.
			send_sony_ir_signal(SONY_AV_RECV_POWER_STANDBY, 15);
		break;
		
		default:
		break;
	}
}


void send_sony_ir_signal(unsigned long code_to_send, int bit_length_of_code)
{
	for (int i = 0; i < 3; i++)
	{
		irsend.sendSony(code_to_send, bit_length_of_code);
		delay(40);
    }
}

void send_samsung_ir_signal(unsigned long code_to_send, int bit_length_of_code)
{
	for (int i = 0; i < 3; i++)
	{
		irsend.sendSAMSUNG(code_to_send, bit_length_of_code);
		delay(40);
    }
}

void handle_error()
{
	Serial.println("ERROR!");	
}

void setup()
{
	pinMode(status_led_pin, OUTPUT);
	Serial.begin(9600);
	pi_code_received = 0;
	light_status_light(1);
}



void loop()
{
	if (Serial.available())
	{
		pi_code_received = (Serial.read() - '0');
		light_status_light(pi_code_received);
		decode_serial_from_pi(pi_code_received);
	}
	delay(500);
}
