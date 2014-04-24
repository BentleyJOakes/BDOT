/*
 * HSimpleConst_export.c
 *
 * Code generation for model "HSimpleConst_export".
 *
 * Model version              : 1.6
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:12:25 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "HSimpleConst_export.h"
#include "HSimpleConst_export_private.h"

/* External inputs (root inport signals with auto storage) */
ExternalInputs_HSimpleConst_exp HSimpleConst_export_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_HSimpleConst_ex HSimpleConst_export_Y;

/* Real-time model */
RT_MODEL_HSimpleConst_export HSimpleConst_export_M_;
RT_MODEL_HSimpleConst_export *const HSimpleConst_export_M =
  &HSimpleConst_export_M_;

/* Model step function */
void HSimpleConst_export_step(void)
{
  /* Outport: '<Root>/Out1' incorporates:
   *  Constant: '<Root>/Constant23'
   *  Inport: '<Root>/In1'
   *  Product: '<Root>/Product'
   */
  HSimpleConst_export_Y.Out1 = 545.54 * HSimpleConst_export_U.In1;

  /* Matfile logging */
  rt_UpdateTXYLogVars(HSimpleConst_export_M->rtwLogInfo,
                      (HSimpleConst_export_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++HSimpleConst_export_M->Timing.clockTick0)) {
    ++HSimpleConst_export_M->Timing.clockTickH0;
  }

  HSimpleConst_export_M->Timing.t[0] = HSimpleConst_export_M->Timing.clockTick0 *
    HSimpleConst_export_M->Timing.stepSize0 +
    HSimpleConst_export_M->Timing.clockTickH0 *
    HSimpleConst_export_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void HSimpleConst_export_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)HSimpleConst_export_M, 0,
                sizeof(RT_MODEL_HSimpleConst_export));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = HSimpleConst_export_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    HSimpleConst_export_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    HSimpleConst_export_M->Timing.sampleTimes =
      (&HSimpleConst_export_M->Timing.sampleTimesArray[0]);
    HSimpleConst_export_M->Timing.offsetTimes =
      (&HSimpleConst_export_M->Timing.offsetTimesArray[0]);

    /* task periods */
    HSimpleConst_export_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    HSimpleConst_export_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(HSimpleConst_export_M, &HSimpleConst_export_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = HSimpleConst_export_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    HSimpleConst_export_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(HSimpleConst_export_M, 1.0E+8);
  HSimpleConst_export_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    HSimpleConst_export_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(HSimpleConst_export_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(HSimpleConst_export_M->rtwLogInfo, (NULL));
    rtliSetLogT(HSimpleConst_export_M->rtwLogInfo, "tout");
    rtliSetLogX(HSimpleConst_export_M->rtwLogInfo, "");
    rtliSetLogXFinal(HSimpleConst_export_M->rtwLogInfo, "");
    rtliSetSigLog(HSimpleConst_export_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(HSimpleConst_export_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(HSimpleConst_export_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(HSimpleConst_export_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(HSimpleConst_export_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &HSimpleConst_export_Y.Out1
      };

      rtliSetLogYSignalPtrs(HSimpleConst_export_M->rtwLogInfo,
                            ((LogSignalPtrsType)rt_LoggedOutputSignalPtrs));
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
        "HSimpleConst_export/Out1" };

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

      rtliSetLogYSignalInfo(HSimpleConst_export_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(HSimpleConst_export_M->rtwLogInfo, "yout");
  }

  HSimpleConst_export_M->solverInfoPtr = (&HSimpleConst_export_M->solverInfo);
  HSimpleConst_export_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&HSimpleConst_export_M->solverInfo, 1.0);
  rtsiSetSolverMode(&HSimpleConst_export_M->solverInfo,
                    SOLVER_MODE_SINGLETASKING);

  /* external inputs */
  HSimpleConst_export_U.In1 = 0.0;

  /* external outputs */
  HSimpleConst_export_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(HSimpleConst_export_M->rtwLogInfo, 0.0,
    rtmGetTFinal(HSimpleConst_export_M), HSimpleConst_export_M->Timing.stepSize0,
                                   (&rtmGetErrorStatus(HSimpleConst_export_M)));

  /* Initialize Sizes */
  HSimpleConst_export_M->Sizes.numContStates = (0);/* Number of continuous states */
  HSimpleConst_export_M->Sizes.numY = (1);/* Number of model outputs */
  HSimpleConst_export_M->Sizes.numU = (1);/* Number of model inputs */
  HSimpleConst_export_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  HSimpleConst_export_M->Sizes.numSampTimes = (1);/* Number of sample times */
  HSimpleConst_export_M->Sizes.numBlocks = (3);/* Number of blocks */
  HSimpleConst_export_M->Sizes.numBlockIO = (0);/* Number of block outputs */
}

/* Model terminate function */
void HSimpleConst_export_terminate(void)
{
}
