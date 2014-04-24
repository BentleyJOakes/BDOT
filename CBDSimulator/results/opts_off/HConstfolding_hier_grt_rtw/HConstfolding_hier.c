/*
 * HConstfolding_hier.c
 *
 * Code generation for model "HConstfolding_hier".
 *
 * Model version              : 1.10
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 15:39:02 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "HConstfolding_hier.h"
#include "HConstfolding_hier_private.h"

/* Block states (auto storage) */
D_Work_HConstfolding_hier HConstfolding_hier_DWork;

/* External inputs (root inport signals with auto storage) */
ExternalInputs_HConstfolding_hi HConstfolding_hier_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_HConstfolding_h HConstfolding_hier_Y;

/* Real-time model */
RT_MODEL_HConstfolding_hier HConstfolding_hier_M_;
RT_MODEL_HConstfolding_hier *const HConstfolding_hier_M = &HConstfolding_hier_M_;

/* Model step function */
void HConstfolding_hier_step(void)
{
  real_T rtb_Product;

  /* Outport: '<Root>/Out1' */
  HConstfolding_hier_Y.Out1 = HConstfolding_hier_DWork.UnitDelay_DSTATE;

  /* Gain: '<Root>/Gain' incorporates:
   *  Constant: '<Root>/Constant'
   */
  rtb_Product = HConstfolding_hier_P.Gain_Gain *
    HConstfolding_hier_P.Constant_Value;

  /* Product: '<S1>/Product' incorporates:
   *  Inport: '<Root>/In1'
   */
  rtb_Product *= HConstfolding_hier_U.In1;

  /* Sum: '<S1>/Sum' */
  HConstfolding_hier_DWork.UnitDelay_DSTATE += rtb_Product;

  /* Matfile logging */
  rt_UpdateTXYLogVars(HConstfolding_hier_M->rtwLogInfo,
                      (HConstfolding_hier_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++HConstfolding_hier_M->Timing.clockTick0)) {
    ++HConstfolding_hier_M->Timing.clockTickH0;
  }

  HConstfolding_hier_M->Timing.t[0] = HConstfolding_hier_M->Timing.clockTick0 *
    HConstfolding_hier_M->Timing.stepSize0 +
    HConstfolding_hier_M->Timing.clockTickH0 *
    HConstfolding_hier_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void HConstfolding_hier_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)HConstfolding_hier_M, 0,
                sizeof(RT_MODEL_HConstfolding_hier));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = HConstfolding_hier_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    HConstfolding_hier_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    HConstfolding_hier_M->Timing.sampleTimes =
      (&HConstfolding_hier_M->Timing.sampleTimesArray[0]);
    HConstfolding_hier_M->Timing.offsetTimes =
      (&HConstfolding_hier_M->Timing.offsetTimesArray[0]);

    /* task periods */
    HConstfolding_hier_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    HConstfolding_hier_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(HConstfolding_hier_M, &HConstfolding_hier_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = HConstfolding_hier_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    HConstfolding_hier_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(HConstfolding_hier_M, 1.0E+8);
  HConstfolding_hier_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    HConstfolding_hier_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(HConstfolding_hier_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(HConstfolding_hier_M->rtwLogInfo, (NULL));
    rtliSetLogT(HConstfolding_hier_M->rtwLogInfo, "tout");
    rtliSetLogX(HConstfolding_hier_M->rtwLogInfo, "");
    rtliSetLogXFinal(HConstfolding_hier_M->rtwLogInfo, "");
    rtliSetSigLog(HConstfolding_hier_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(HConstfolding_hier_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(HConstfolding_hier_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(HConstfolding_hier_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(HConstfolding_hier_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &HConstfolding_hier_Y.Out1
      };

      rtliSetLogYSignalPtrs(HConstfolding_hier_M->rtwLogInfo,
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
        "HConstfolding_hier/Out1" };

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

      rtliSetLogYSignalInfo(HConstfolding_hier_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(HConstfolding_hier_M->rtwLogInfo, "yout");
  }

  HConstfolding_hier_M->solverInfoPtr = (&HConstfolding_hier_M->solverInfo);
  HConstfolding_hier_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&HConstfolding_hier_M->solverInfo, 1.0);
  rtsiSetSolverMode(&HConstfolding_hier_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* states (dwork) */
  (void) memset((void *)&HConstfolding_hier_DWork, 0,
                sizeof(D_Work_HConstfolding_hier));

  /* external inputs */
  HConstfolding_hier_U.In1 = 0.0;

  /* external outputs */
  HConstfolding_hier_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(HConstfolding_hier_M->rtwLogInfo, 0.0,
    rtmGetTFinal(HConstfolding_hier_M), HConstfolding_hier_M->Timing.stepSize0,
                                   (&rtmGetErrorStatus(HConstfolding_hier_M)));

  /* Initialize Sizes */
  HConstfolding_hier_M->Sizes.numContStates = (0);/* Number of continuous states */
  HConstfolding_hier_M->Sizes.numY = (1);/* Number of model outputs */
  HConstfolding_hier_M->Sizes.numU = (1);/* Number of model inputs */
  HConstfolding_hier_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  HConstfolding_hier_M->Sizes.numSampTimes = (1);/* Number of sample times */
  HConstfolding_hier_M->Sizes.numBlocks = (6);/* Number of blocks */
  HConstfolding_hier_M->Sizes.numBlockIO = (0);/* Number of block outputs */
  HConstfolding_hier_M->Sizes.numBlockPrms = (3);/* Sum of parameter "widths" */

  /* InitializeConditions for UnitDelay: '<S1>/Unit Delay' */
  HConstfolding_hier_DWork.UnitDelay_DSTATE = HConstfolding_hier_P.UnitDelay_X0;
}

/* Model terminate function */
void HConstfolding_hier_terminate(void)
{
}
