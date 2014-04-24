/*
 * HConstfolding.c
 *
 * Code generation for model "HConstfolding".
 *
 * Model version              : 1.12
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 15:37:39 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "HConstfolding.h"
#include "HConstfolding_private.h"

/* Block states (auto storage) */
D_Work_HConstfolding HConstfolding_DWork;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_HConstfolding HConstfolding_Y;

/* Real-time model */
RT_MODEL_HConstfolding HConstfolding_M_;
RT_MODEL_HConstfolding *const HConstfolding_M = &HConstfolding_M_;

/* Model step function */
void HConstfolding_step(void)
{
  real_T rtb_Gain1;

  /* Product: '<Root>/Product' */
  HConstfolding_DWork.UnitDelay_DSTATE *= HConstfolding_DWork.UnitDelay1_DSTATE;

  /* Gain: '<Root>/Gain2' */
  HConstfolding_DWork.UnitDelay_DSTATE *= HConstfolding_P.Gain2_Gain;

  /* Gain: '<Root>/Gain3' */
  HConstfolding_DWork.UnitDelay_DSTATE *= HConstfolding_P.Gain3_Gain;

  /* Outport: '<Root>/Out1' */
  HConstfolding_Y.Out1 = HConstfolding_DWork.UnitDelay_DSTATE;

  /* Gain: '<Root>/Gain' incorporates:
   *  Constant: '<Root>/Constant'
   */
  HConstfolding_DWork.UnitDelay1_DSTATE = HConstfolding_P.Gain_Gain *
    HConstfolding_P.Constant_Value;

  /* Gain: '<Root>/Gain1' incorporates:
   *  Constant: '<Root>/Constant2'
   */
  rtb_Gain1 = HConstfolding_P.Gain1_Gain * HConstfolding_P.Constant2_Value;

  /* Sum: '<Root>/Sum' incorporates:
   *  Constant: '<Root>/Constant1'
   */
  HConstfolding_DWork.UnitDelay1_DSTATE += HConstfolding_P.Constant1_Value;

  /* Sum: '<Root>/Sum1' incorporates:
   *  Constant: '<Root>/Constant4'
   */
  HConstfolding_DWork.UnitDelay_DSTATE = HConstfolding_P.Constant4_Value +
    HConstfolding_DWork.UnitDelay1_DSTATE;

  /* Update for UnitDelay: '<Root>/Unit Delay1' */
  HConstfolding_DWork.UnitDelay1_DSTATE = rtb_Gain1;

  /* Matfile logging */
  rt_UpdateTXYLogVars(HConstfolding_M->rtwLogInfo, (HConstfolding_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++HConstfolding_M->Timing.clockTick0)) {
    ++HConstfolding_M->Timing.clockTickH0;
  }

  HConstfolding_M->Timing.t[0] = HConstfolding_M->Timing.clockTick0 *
    HConstfolding_M->Timing.stepSize0 + HConstfolding_M->Timing.clockTickH0 *
    HConstfolding_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void HConstfolding_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)HConstfolding_M, 0,
                sizeof(RT_MODEL_HConstfolding));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = HConstfolding_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    HConstfolding_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    HConstfolding_M->Timing.sampleTimes =
      (&HConstfolding_M->Timing.sampleTimesArray[0]);
    HConstfolding_M->Timing.offsetTimes =
      (&HConstfolding_M->Timing.offsetTimesArray[0]);

    /* task periods */
    HConstfolding_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    HConstfolding_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(HConstfolding_M, &HConstfolding_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = HConstfolding_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    HConstfolding_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(HConstfolding_M, 1.0E+8);
  HConstfolding_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    HConstfolding_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(HConstfolding_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(HConstfolding_M->rtwLogInfo, (NULL));
    rtliSetLogT(HConstfolding_M->rtwLogInfo, "tout");
    rtliSetLogX(HConstfolding_M->rtwLogInfo, "");
    rtliSetLogXFinal(HConstfolding_M->rtwLogInfo, "");
    rtliSetSigLog(HConstfolding_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(HConstfolding_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(HConstfolding_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(HConstfolding_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(HConstfolding_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &HConstfolding_Y.Out1
      };

      rtliSetLogYSignalPtrs(HConstfolding_M->rtwLogInfo, ((LogSignalPtrsType)
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
        "HConstfolding/Out1" };

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

      rtliSetLogYSignalInfo(HConstfolding_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(HConstfolding_M->rtwLogInfo, "yout");
  }

  HConstfolding_M->solverInfoPtr = (&HConstfolding_M->solverInfo);
  HConstfolding_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&HConstfolding_M->solverInfo, 1.0);
  rtsiSetSolverMode(&HConstfolding_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* states (dwork) */
  (void) memset((void *)&HConstfolding_DWork, 0,
                sizeof(D_Work_HConstfolding));

  /* external outputs */
  HConstfolding_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(HConstfolding_M->rtwLogInfo, 0.0,
    rtmGetTFinal(HConstfolding_M), HConstfolding_M->Timing.stepSize0,
    (&rtmGetErrorStatus(HConstfolding_M)));

  /* Initialize Sizes */
  HConstfolding_M->Sizes.numContStates = (0);/* Number of continuous states */
  HConstfolding_M->Sizes.numY = (1);   /* Number of model outputs */
  HConstfolding_M->Sizes.numU = (0);   /* Number of model inputs */
  HConstfolding_M->Sizes.sysDirFeedThru = (0);/* The model is not direct feedthrough */
  HConstfolding_M->Sizes.numSampTimes = (1);/* Number of sample times */
  HConstfolding_M->Sizes.numBlocks = (14);/* Number of blocks */
  HConstfolding_M->Sizes.numBlockIO = (0);/* Number of block outputs */
  HConstfolding_M->Sizes.numBlockPrms = (10);/* Sum of parameter "widths" */

  /* InitializeConditions for UnitDelay: '<Root>/Unit Delay' */
  HConstfolding_DWork.UnitDelay_DSTATE = HConstfolding_P.UnitDelay_X0;

  /* InitializeConditions for UnitDelay: '<Root>/Unit Delay1' */
  HConstfolding_DWork.UnitDelay1_DSTATE = HConstfolding_P.UnitDelay1_X0;
}

/* Model terminate function */
void HConstfolding_terminate(void)
{
}
