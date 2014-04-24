/*
 * HSimpleConstDead.c
 *
 * Code generation for model "HSimpleConstDead".
 *
 * Model version              : 1.11
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:57:54 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "HSimpleConstDead.h"
#include "HSimpleConstDead_private.h"

/* External inputs (root inport signals with auto storage) */
ExternalInputs_HSimpleConstDead HSimpleConstDead_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_HSimpleConstDea HSimpleConstDead_Y;

/* Real-time model */
RT_MODEL_HSimpleConstDead HSimpleConstDead_M_;
RT_MODEL_HSimpleConstDead *const HSimpleConstDead_M = &HSimpleConstDead_M_;

/* Model step function */
void HSimpleConstDead_step(void)
{
  /* Outport: '<Root>/Out1' incorporates:
   *  Constant: '<Root>/Constant2'
   *  Inport: '<Root>/In1'
   *  Product: '<Root>/Product'
   */
  HSimpleConstDead_Y.Out1 = 433.22 * HSimpleConstDead_U.In1;

  /* Matfile logging */
  rt_UpdateTXYLogVars(HSimpleConstDead_M->rtwLogInfo,
                      (HSimpleConstDead_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++HSimpleConstDead_M->Timing.clockTick0)) {
    ++HSimpleConstDead_M->Timing.clockTickH0;
  }

  HSimpleConstDead_M->Timing.t[0] = HSimpleConstDead_M->Timing.clockTick0 *
    HSimpleConstDead_M->Timing.stepSize0 +
    HSimpleConstDead_M->Timing.clockTickH0 *
    HSimpleConstDead_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void HSimpleConstDead_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)HSimpleConstDead_M, 0,
                sizeof(RT_MODEL_HSimpleConstDead));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = HSimpleConstDead_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    HSimpleConstDead_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    HSimpleConstDead_M->Timing.sampleTimes =
      (&HSimpleConstDead_M->Timing.sampleTimesArray[0]);
    HSimpleConstDead_M->Timing.offsetTimes =
      (&HSimpleConstDead_M->Timing.offsetTimesArray[0]);

    /* task periods */
    HSimpleConstDead_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    HSimpleConstDead_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(HSimpleConstDead_M, &HSimpleConstDead_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = HSimpleConstDead_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    HSimpleConstDead_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(HSimpleConstDead_M, 1.0E+8);
  HSimpleConstDead_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    HSimpleConstDead_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(HSimpleConstDead_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(HSimpleConstDead_M->rtwLogInfo, (NULL));
    rtliSetLogT(HSimpleConstDead_M->rtwLogInfo, "tout");
    rtliSetLogX(HSimpleConstDead_M->rtwLogInfo, "");
    rtliSetLogXFinal(HSimpleConstDead_M->rtwLogInfo, "");
    rtliSetSigLog(HSimpleConstDead_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(HSimpleConstDead_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(HSimpleConstDead_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(HSimpleConstDead_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(HSimpleConstDead_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &HSimpleConstDead_Y.Out1
      };

      rtliSetLogYSignalPtrs(HSimpleConstDead_M->rtwLogInfo, ((LogSignalPtrsType)
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
        "HSimpleConstDead/Out1" };

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

      rtliSetLogYSignalInfo(HSimpleConstDead_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(HSimpleConstDead_M->rtwLogInfo, "yout");
  }

  HSimpleConstDead_M->solverInfoPtr = (&HSimpleConstDead_M->solverInfo);
  HSimpleConstDead_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&HSimpleConstDead_M->solverInfo, 1.0);
  rtsiSetSolverMode(&HSimpleConstDead_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* external inputs */
  HSimpleConstDead_U.In1 = 0.0;

  /* external outputs */
  HSimpleConstDead_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(HSimpleConstDead_M->rtwLogInfo, 0.0,
    rtmGetTFinal(HSimpleConstDead_M), HSimpleConstDead_M->Timing.stepSize0,
    (&rtmGetErrorStatus(HSimpleConstDead_M)));

  /* Initialize Sizes */
  HSimpleConstDead_M->Sizes.numContStates = (0);/* Number of continuous states */
  HSimpleConstDead_M->Sizes.numY = (1);/* Number of model outputs */
  HSimpleConstDead_M->Sizes.numU = (1);/* Number of model inputs */
  HSimpleConstDead_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  HSimpleConstDead_M->Sizes.numSampTimes = (1);/* Number of sample times */
  HSimpleConstDead_M->Sizes.numBlocks = (3);/* Number of blocks */
  HSimpleConstDead_M->Sizes.numBlockIO = (0);/* Number of block outputs */
}

/* Model terminate function */
void HSimpleConstDead_terminate(void)
{
}
