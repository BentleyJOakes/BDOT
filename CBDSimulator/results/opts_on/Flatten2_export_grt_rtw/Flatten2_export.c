/*
 * Flatten2_export.c
 *
 * Code generation for model "Flatten2_export".
 *
 * Model version              : 1.5
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 14:26:10 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "Flatten2_export.h"
#include "Flatten2_export_private.h"

/* Block states (auto storage) */
D_Work_Flatten2_export Flatten2_export_DWork;

/* External inputs (root inport signals with auto storage) */
ExternalInputs_Flatten2_export Flatten2_export_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_Flatten2_export Flatten2_export_Y;

/* Real-time model */
RT_MODEL_Flatten2_export Flatten2_export_M_;
RT_MODEL_Flatten2_export *const Flatten2_export_M = &Flatten2_export_M_;

/* Model step function */
void Flatten2_export_step(void)
{
  /* local block i/o variables */
  real_T rtb_Gain2;

  /* Gain: '<Root>/Gain2' incorporates:
   *  Constant: '<Root>/Constant'
   *  Constant: '<Root>/Constant2'
   *  Constant: '<S1>/Constant'
   *  Inport: '<Root>/In1'
   *  Product: '<Root>/Product2'
   *  Product: '<S1>/Product3'
   *  Sum: '<S1>/Sum'
   */
  rtb_Gain2 = (Flatten2_export_U.In1 * 134.67 * 12.34 + 66598.0) * 5.4;

  /* Outport: '<Root>/Out1' */
  Flatten2_export_Y.Out1 = rtb_Gain2;

  /* Matfile logging */
  rt_UpdateTXYLogVars(Flatten2_export_M->rtwLogInfo,
                      (Flatten2_export_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++Flatten2_export_M->Timing.clockTick0)) {
    ++Flatten2_export_M->Timing.clockTickH0;
  }

  Flatten2_export_M->Timing.t[0] = Flatten2_export_M->Timing.clockTick0 *
    Flatten2_export_M->Timing.stepSize0 + Flatten2_export_M->Timing.clockTickH0 *
    Flatten2_export_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void Flatten2_export_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)Flatten2_export_M, 0,
                sizeof(RT_MODEL_Flatten2_export));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = Flatten2_export_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    Flatten2_export_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    Flatten2_export_M->Timing.sampleTimes =
      (&Flatten2_export_M->Timing.sampleTimesArray[0]);
    Flatten2_export_M->Timing.offsetTimes =
      (&Flatten2_export_M->Timing.offsetTimesArray[0]);

    /* task periods */
    Flatten2_export_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    Flatten2_export_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(Flatten2_export_M, &Flatten2_export_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = Flatten2_export_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    Flatten2_export_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(Flatten2_export_M, 1.0E+8);
  Flatten2_export_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    Flatten2_export_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(Flatten2_export_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(Flatten2_export_M->rtwLogInfo, (NULL));
    rtliSetLogT(Flatten2_export_M->rtwLogInfo, "tout");
    rtliSetLogX(Flatten2_export_M->rtwLogInfo, "");
    rtliSetLogXFinal(Flatten2_export_M->rtwLogInfo, "");
    rtliSetSigLog(Flatten2_export_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(Flatten2_export_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(Flatten2_export_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(Flatten2_export_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(Flatten2_export_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &Flatten2_export_Y.Out1
      };

      rtliSetLogYSignalPtrs(Flatten2_export_M->rtwLogInfo, ((LogSignalPtrsType)
        rt_LoggedOutputSignalPtrs));
    }

    {
      static int_T rt_LoggedOutputWidths[] = {
        1
      };

      static int_T rt_LoggedOutputNumDimensions[] = {
        1
      };

      static int_T rt_LoggedOutputDimensions[] = {
        1
      };

      static boolean_T rt_LoggedOutputIsVarDims[] = {
        0
      };

      static void* rt_LoggedCurrentSignalDimensions[] = {
        (NULL)
      };

      static int_T rt_LoggedCurrentSignalDimensionsSize[] = {
        4
      };

      static BuiltInDTypeId rt_LoggedOutputDataTypeIds[] = {
        SS_DOUBLE
      };

      static int_T rt_LoggedOutputComplexSignals[] = {
        0
      };

      static const char_T *rt_LoggedOutputLabels[] = {
        "" };

      static const char_T *rt_LoggedOutputBlockNames[] = {
        "Flatten2_export/Out1" };

      static RTWLogDataTypeConvert rt_RTWLogDataTypeConvert[] = {
        { 0, SS_DOUBLE, SS_DOUBLE, 0, 0, 0, 1.0, 0, 0.0 }
      };

      static RTWLogSignalInfo rt_LoggedOutputSignalInfo[] = {
        {
          1,
          rt_LoggedOutputWidths,
          rt_LoggedOutputNumDimensions,
          rt_LoggedOutputDimensions,
          rt_LoggedOutputIsVarDims,
          rt_LoggedCurrentSignalDimensions,
          rt_LoggedCurrentSignalDimensionsSize,
          rt_LoggedOutputDataTypeIds,
          rt_LoggedOutputComplexSignals,
          (NULL),

          { rt_LoggedOutputLabels },
          (NULL),
          (NULL),
          (NULL),

          { rt_LoggedOutputBlockNames },

          { (NULL) },
          (NULL),
          rt_RTWLogDataTypeConvert
        }
      };

      rtliSetLogYSignalInfo(Flatten2_export_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(Flatten2_export_M->rtwLogInfo, "yout");
  }

  Flatten2_export_M->solverInfoPtr = (&Flatten2_export_M->solverInfo);
  Flatten2_export_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&Flatten2_export_M->solverInfo, 1.0);
  rtsiSetSolverMode(&Flatten2_export_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* states (dwork) */
  (void) memset((void *)&Flatten2_export_DWork, 0,
                sizeof(D_Work_Flatten2_export));

  /* external inputs */
  Flatten2_export_U.In1 = 0.0;

  /* external outputs */
  Flatten2_export_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(Flatten2_export_M->rtwLogInfo, 0.0,
    rtmGetTFinal(Flatten2_export_M), Flatten2_export_M->Timing.stepSize0,
    (&rtmGetErrorStatus(Flatten2_export_M)));

  /* Initialize Sizes */
  Flatten2_export_M->Sizes.numContStates = (0);/* Number of continuous states */
  Flatten2_export_M->Sizes.numY = (1); /* Number of model outputs */
  Flatten2_export_M->Sizes.numU = (1); /* Number of model inputs */
  Flatten2_export_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  Flatten2_export_M->Sizes.numSampTimes = (1);/* Number of sample times */
  Flatten2_export_M->Sizes.numBlocks = (9);/* Number of blocks */
  Flatten2_export_M->Sizes.numBlockIO = (0);/* Number of block outputs */
}

/* Model terminate function */
void Flatten2_export_terminate(void)
{
}
