/* File Gaurd by ifndef & endif */
#ifndef DIO_INTERFACE_H
#define DIO_INTERFACE_H

/** Macros as Direction options */
#define INPUT                    0
#define OUTPUT                   1

/**** Macros as Value options ***/
#define LOW                      0
#define HIGH                     1

/* Macros as PortNumber options */
#define PORTA                    0    
#define PORTB                    1     
#define PORTC                    2    
#define PORTD                    3

/** Macros as PinNumber options */
#define PIN0                     0    
#define PIN1                     1     
#define PIN2                     2    
#define PIN3                     3
#define PIN4                     4    
#define PIN5                     5     
#define PIN6                     6    
#define PIN7                     7



/****************************************************************************/
/************************** My Functions Prototype **************************/
/****************************************************************************/

/****************************************************************************/
/* Function Name : DIO_voidSetPinDirection                                  */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Argument3: Copy_u8Direction { INPUT,OUTPUT }                        */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPinDirection (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber, u8 Copy_u8Direction );

/****************************************************************************/
/* Function Name : DIO_voidSetPinValue                                      */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Argument3: Copy_u8Value { HIGH , LOW }                              */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber, u8 Copy_u8Value );

/****************************************************************************/
/* Function Name : DIO_u8GetPinValue                                        */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Return :  unsigned char                                             */
/****************************************************************************/
u8 DIO_u8GetPinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber );

/****************************************************************************/
/* Function Name : DIO_voidTogglePinValue                                   */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidTogglePinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber );

/****************************************************************************/
/* Function Name : DIO_voidSetPortDirection                                 */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument3: Copy_u8Direction { INPUT,OUTPUT }                        */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPortDirection (u8 Copy_u8PortNumber, u8 Copy_u8Direction );

/****************************************************************************/
/* Function Name : DIO_voidSetPortValue                                      */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument3: Copy_u8Value { HIGH , LOW }                              */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPortValue (u8 Copy_u8PortNumber, u8 Copy_u8Value );

/****************************************************************************/
/* Function Name : DIO_u8GetPortValue                                       */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Return :  unsigned char                                             */
/****************************************************************************/
u8 DIO_u8GetPortValue (u8 Copy_u8PortNumber );

/****************************************************************************/
/* Function Name : DIO_voidTogglePortValue                                  */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidTogglePortValue (u8 Copy_u8PortNumber );




#endif