      ******************************************************************
      * Author: Cayque
      * Date: 09/05/2022
      * Purpose: sofrimento
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. Calculadora.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.

       01 FirstNum PIC 9 VALUE ZEROS.
       01 SecondNum PIC 9 VALUE ZEROS.
       01 CalcResult PIC 99 VALUE 0.
       01 UserPrompt PIC X(38) VALUE
                     "Please enter two single digit numbers".


       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

       CalculateResult.
          DISPLAY UserPrompt
          ACCEPT FirstNum
          ACCEPT SecondNum
          COMPUTE CalcResult = FirstNum + SecondNum
          DISPLAY "Result is = ", CalcResult
       STOP RUN.
       END PROGRAM Calculadora.
