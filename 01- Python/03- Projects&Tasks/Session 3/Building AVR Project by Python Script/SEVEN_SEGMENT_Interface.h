/*========================================================================================================*/
/*  File        : SEVEN_SEGMENT_Interface.h                                                               */
/*  Description : This interface file includes 7_SEGMENT Driver prototypes and declarations for Atmega32  */
/*  Author      : Ahmed Bahaa Taha Nasr. Embedded SW Engineer                                             */
/*  Date        : 28/3/2023                                                                               */
/*  Linkedin    : https://www.linkedin.com/in/ahmed-bahaa1/                                               */
/*  Git account : https://github.com/ahmedbahaa11                                                         */
/*  mail        : ahmedbahaataha7@gmil.com                                                                */
/*========================================================================================================*/

/* File Gaurd by ifndef & endif */
#ifndef SEVEN_SEGMENT_INTERFACE_H
#define SEVEN_SEGMENT_INTERFACE_H


#define COMMON_ANODE               0
#define COMMON_CATHODE             1

#define INCREMENT                  1
#define DECREMENT                  0



/*======================================================================================================================*/
/***********************************       A.BAHAA 7_SEGMENT Functions Prototype       **********************************/
/*======================================================================================================================*/
/********************************************    SEGMENT_voidInit                  **************************************/
/********************************************    SEGMENT_voidPrintNumber           **************************************/
/********************************************    SEGMENT_voidPrintCounter          **************************************/
/*======================================================================================================================*/

void SEGMENT_voidInitSegmentPort ( u8 Copy_u8PortNumber );
void SEGMENT_voidPrintNumber ( u8 Copy_u8PortNumber , u8 Copy_SegmentPolarity , u8 Copy_u8Number );
void SEGMENT_voidPrintCounter ( u8 Copy_u8PortNumber , u8 Copy_u8Behavier , u8 Copy_SegmentPolarity , u8 Copy_u8TimeBetweenNumbers );

#endif
