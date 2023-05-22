// #include <util/delay.h>
#include "STD_TYPES.h"
#include "BIT_MATH.h"
#include "DIO_Interface.h"
#include "SEVEN_SEGMENT_Interface.h"
const long unsigned int DELAY_CYCLES = 1900000UL ;

void GreenLED (void)
{
	DIO_voidSetPinValue (PORTC, PIN0,LOW );
	DIO_voidSetPinValue (PORTC, PIN1,LOW );
	DIO_voidSetPinValue (PORTC, PIN2, HIGH );
}
void YellowLED (void)
{
	DIO_voidSetPinValue (PORTC, PIN0,LOW );
	DIO_voidSetPinValue (PORTC, PIN1,HIGH );
	DIO_voidSetPinValue (PORTC, PIN2,LOW );
}
void RedLED (void)
{
	DIO_voidSetPinValue (PORTC, PIN0,HIGH );
	DIO_voidSetPinValue (PORTC, PIN1,LOW );
	DIO_voidSetPinValue (PORTC, PIN2,LOW );
}

int main ()
{
	SEGMENT_voidInitSegmentPort ( PORTA );
	SEGMENT_voidInitSegmentPort ( PORTB );
	DIO_voidSetPinDirection (PORTC,PIN0,OUTPUT);
	DIO_voidSetPinDirection (PORTC,PIN1,OUTPUT);
	DIO_voidSetPinDirection (PORTC,PIN2,OUTPUT);
	while(1)
	{
		// Green LED for 10 sec
		
		RedLED();
		for( u16 i=10 ; i>0 ; i-- )
		{
			if(i==10)
			{
				SEGMENT_voidPrintNumber ( PORTA , COMMON_ANODE , 1 );
				SEGMENT_voidPrintNumber ( PORTB , COMMON_ANODE , 0 );
			}
			else
			{
				SEGMENT_voidPrintNumber ( PORTA , COMMON_ANODE , 0 );
				SEGMENT_voidPrintNumber ( PORTB , COMMON_ANODE , i );

			}
			// _delay_ms(500);
			__builtin_avr_delay_cycles(DELAY_CYCLES);
		}
		// Yellow LED for 3 sec
		YellowLED();
		for( u16 i=3 ; i>0 ; i-- )
		{
			SEGMENT_voidPrintNumber ( PORTA , COMMON_ANODE , 0 );
			SEGMENT_voidPrintNumber ( PORTB , COMMON_ANODE , i );
			// _delay_ms(500);
			__builtin_avr_delay_cycles(DELAY_CYCLES);
		}
		// RED LED for 10 sec
		GreenLED();
		for( u16 i=10 ; i>0 ; i-- )
		{
			if(i==10)
			{
				SEGMENT_voidPrintNumber ( PORTA , COMMON_ANODE , 1 );
				SEGMENT_voidPrintNumber ( PORTB , COMMON_ANODE , 0 );
			}
			else
			{
				SEGMENT_voidPrintNumber ( PORTA , COMMON_ANODE , 0 );
				SEGMENT_voidPrintNumber ( PORTB , COMMON_ANODE , i );
			}
			// _delay_ms(500);
			__builtin_avr_delay_cycles(DELAY_CYCLES);
		}
	}
}


