/* Include Header Files */
#include "STD_TYPES.h"
#include "BIT_MATH.h"

/* Include My own Header Files*/
#include "DIO_Interface.h"
#include "DIO_Private.h"
#include "DIO_Config.h"


/****************************************************************************/
/************************ My Functions Implementation ***********************/
/****************************************************************************/

/****************************************************************************/
/* Function Name : DIO_voidSetPinDirection                                  */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Argument3: Copy_u8Direction { INPUT,OUTPUT }                        */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPinDirection (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber, u8 Copy_u8Direction )
{
    /* i/p validation */
    if ( Copy_u8PortNumber > PORTD || Copy_u8PinNumber > PIN7 )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8Direction)
        {
            case INPUT :    switch(Copy_u8PortNumber)
                            {
                                case PORTA :    CLEAR_BIT( DDRA_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTB :    CLEAR_BIT( DDRB_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTC :    CLEAR_BIT( DDRC_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTD :    CLEAR_BIT( DDRD_REG ,Copy_u8PinNumber );
                                                break;
                                default : 
                                                break;
                            }
                            break;
            case OUTPUT :   switch(Copy_u8PortNumber)
                            {
                                case PORTA :    SET_BIT( DDRA_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTB :    SET_BIT( DDRB_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTC :    SET_BIT( DDRC_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTD :    SET_BIT( DDRD_REG ,Copy_u8PinNumber );
                                                break;
                                default : 
                                                break;
                            }
                            break;
            default :
                            break;
        }
    }
}

/****************************************************************************/
/* Function Name : DIO_voidSetPinValue                                      */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Argument3: Copy_u8Value { HIGH , LOW }                              */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber, u8 Copy_u8Value )
{
        /* i/p validation */
    if ( Copy_u8PortNumber > PORTD || Copy_u8PinNumber > PIN7 )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8Value)
        {
            case LOW :    switch(Copy_u8PortNumber)
                            {
                                case PORTA :    CLEAR_BIT( PORTA_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTB :    CLEAR_BIT( PORTB_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTC :    CLEAR_BIT( PORTC_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTD :    CLEAR_BIT( PORTD_REG ,Copy_u8PinNumber );
                                                break;
                                default : 
                                                break;
                            }
                            break;
            case HIGH :   switch(Copy_u8PortNumber)
                            {
                                case PORTA :    SET_BIT( PORTA_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTB :    SET_BIT( PORTB_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTC :    SET_BIT( PORTC_REG ,Copy_u8PinNumber );
                                                break;
                                case PORTD :    SET_BIT( PORTD_REG ,Copy_u8PinNumber );
                                                break;
                                default : 
                                                break;
                            }
                            break;
            default :
                            break;
        }
    }
}

/****************************************************************************/
/* Function Name : DIO_u8GetPinValue                                        */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Return :  unsigned char                                             */
/****************************************************************************/
u8 DIO_u8GetPinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber )
{
    u8 Local_u8Variable;
    /* i/p validation */
    if ( Copy_u8PortNumber > PORTD || Copy_u8PinNumber > PIN7 )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8PortNumber)
        {
            case PORTA :    Local_u8Variable = GET_BIT( PINA_REG ,Copy_u8PinNumber );
                            break;
            case PORTB :    Local_u8Variable = GET_BIT( PINB_REG ,Copy_u8PinNumber );
                            break;
            case PORTC :    Local_u8Variable = GET_BIT( PINC_REG ,Copy_u8PinNumber );
                            break;
            case PORTD :    Local_u8Variable = GET_BIT( PIND_REG ,Copy_u8PinNumber );
                            break;
            default : 
                            break;
        }
    }
    return Local_u8Variable ;
}

/****************************************************************************/
/* Function Name : DIO_voidTogglePinValue                                   */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument2: Copy_u8PinNumber { PIN0,PIN1,PIN3,PIN4,PIN5,PIN6,PIN7 }  */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidTogglePinValue (u8 Copy_u8PortNumber, u8 Copy_u8PinNumber )
{
        /* i/p validation */
    if ( Copy_u8PortNumber > PORTD || Copy_u8PinNumber > PIN7 )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8PortNumber)
        {
            case PORTA :    TOGGLE_BIT( PORTA_REG, Copy_u8PinNumber );
                            break;
            case PORTB :    TOGGLE_BIT( PORTB_REG, Copy_u8PinNumber );
                            break;
            case PORTC :    TOGGLE_BIT( PORTC_REG, Copy_u8PinNumber );
                            break;
            case PORTD :    TOGGLE_BIT( PORTD_REG, Copy_u8PinNumber );
                            break;
            default :
                            break; 
        }
    }
}

/****************************************************************************/
/* Function Name : DIO_voidSetPortDirection                                 */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument3: Copy_u8Direction { INPUT,OUTPUT }                        */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPortDirection (u8 Copy_u8PortNumber, u8 Copy_u8Direction )
{
    /* i/p validation */
    if ( Copy_u8PortNumber > PORTD )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8Direction)
        {
            case INPUT :    switch(Copy_u8PortNumber)
                            {
                                case PORTA :    DDRA_REG = 0x00 ;
                                                break;
                                case PORTB :    DDRB_REG = 0x00 ;
                                                break;
                                case PORTC :    DDRC_REG = 0x00 ;
                                                break;
                                case PORTD :    DDRD_REG = 0x00 ;
                                                break;
                                default :
                                                break; 
                            }
                            break;
            case OUTPUT :   switch(Copy_u8PortNumber)
                            {
                                case PORTA :    DDRA_REG = 0xff ;
                                                break;
                                case PORTB :    DDRB_REG = 0xff ;
                                                break;
                                case PORTC :    DDRC_REG = 0xff ;
                                                break;
                                case PORTD :    DDRD_REG = 0xff ;
                                                break;
                                default :
                                                break; 
                            }
                            break;
            default :
                            break;
        }
    }
}

/****************************************************************************/
/* Function Name : DIO_voidSetPortValue                                      */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Argument3: Copy_u8Value { HIGH , LOW }                              */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidSetPortValue (u8 Copy_u8PortNumber, u8 Copy_u8Value )
{
    /* i/p validation */
    if ( Copy_u8PortNumber > PORTD )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8PortNumber)
        {
            case PORTA :    PORTA_REG = Copy_u8Value ;
                            break;
            case PORTB :    PORTB_REG = Copy_u8Value ;
                            break;
            case PORTC :    PORTC_REG = Copy_u8Value ;
                            break;
            case PORTD :    PORTD_REG = Copy_u8Value ;
                            break;
            default :
                            break; 
        }
    }
}

/****************************************************************************/
/* Function Name : DIO_u8GetPortValue                                       */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Return :  unsigned char                                             */
/****************************************************************************/
u8 DIO_u8GetPortValue (u8 Copy_u8PortNumber )
{
    u8 Local_u8Variable;
    /* i/p validation */
    if ( Copy_u8PortNumber > PORTD )
    {
        // Do Nothing
    }
    else
    {
        switch(Copy_u8PortNumber)
        {
            case PORTA :    Local_u8Variable = PINA_REG ;  
                            break;
            case PORTB :    Local_u8Variable = PINB_REG ;
                            break;
            case PORTC :    Local_u8Variable = PINC_REG ;
                            break;
            case PORTD :    Local_u8Variable = PIND_REG ;
                            break;
            default :
                            break; 
        }
    }
    return Local_u8Variable ;
}

/****************************************************************************/
/* Function Name : DIO_voidTogglePortValue                                  */
/* Fun. Argument1: Copy_u8PortNumber { PORTA,PORTB,PORTC,PORTD }            */
/* Fun. Return : void                                                       */
/****************************************************************************/
void DIO_voidTogglePortValue (u8 Copy_u8PortNumber )
{
        /* i/p validation */
    if ( Copy_u8PortNumber > PORTD )
    {
        // Do Nothing
    }
    else 
    {
        switch(Copy_u8PortNumber)
        {
            case PORTA :    PORTA_REG ^= 0b11111111 ;           
                            break;
            case PORTB :    PORTB_REG ^= 255 ;           // REG ^= 0b11111111  =  REG ^= 255
                            break;
            case PORTC :    PORTC_REG ^= 255 ; 
                            break;
            case PORTD :    PORTD_REG ^= 255 ; 
                            break;
            default :
                            break; 
        }
    }
}
