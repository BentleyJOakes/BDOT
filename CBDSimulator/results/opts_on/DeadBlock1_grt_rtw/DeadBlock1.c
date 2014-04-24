/*
 * DeadBlock1.c
 *
 * Code generation for model "DeadBlock1".
 *
 * Model version              : 1.5
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:59:10 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "DeadBlock1.h"
#include "DeadBlock1_private.h"

/* Block states (auto storage) */
D_Work_DeadBlock1 DeadBlock1_DWork;

/* External inputs (root inport signals with auto storage) */
ExternalInputs_DeadBlock1 DeadBlock1_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_DeadBlock1 DeadBlock1_Y;

/* Real-time model */
RT_MODEL_DeadBlock1 DeadBlock1_M_;
RT_MODEL_DeadBlock1 *const DeadBlock1_M = &DeadBlock1_M_;

/* Model step function */
void DeadBlock1_step(void)
{
  /* local block i/o variables */
  real_T rtb_Product;

  /* Product: '<Root>/Product' incorporates:
   *  Inport: '<Root>/In1'
   *  Inport: '<Root>/In2'
   */
  rtb_Product = DeadBlock1_U.In2 * DeadBlock1_U.In1;

  /* Outport: '<Root>/Out1' */
  DeadBlock1_Y.Out1 = rtb_Product;

  /* Matfile logging */
  rt_UpdateTXYLogVars(DeadBlock1_M->rtwLogInfo, (DeadBlock1_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++DeadBlock1_M->Timing.clockTick0)) {
    ++DeadBlock1_M->Timing.clockTickH0;
  }

  DeadBlock1_M->Timing.t[0] = DeadBlock1_M->Timing.clockTick0 *
    DeadBlock1_M->Timing.stepSize0 + DeadBlock1_M->Timing.clockTickH0 *
    DeadBlock1_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void DeadBlock1_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)DeadBlock1_M, 0,
                sizeof(RT_MODEL_DeadBlock1));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = DeadBlock1_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    DeadBlock1_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    DeadBlock1_M->Timing.sampleTimes = (&DeadBlock1_M->Timing.sampleTimesArray[0]);
    DeadBlock1_M->Timing.offsetTimes = (&DeadBlock1_M->Timing.offsetTimesArray[0]);

    /* task periods */
    DeadBlock1_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    DeadBlock1_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(DeadBlock1_M, &DeadBlock1_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = DeadBlock1_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    DeadBlock1_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(DeadBlock1_M, 1.0E+8);
  DeadBlock1_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    DeadBlock1_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(DeadBlock1_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(DeadBlock1_M->rtwLogInfo, (NULL));
    rtliSetLogT(DeadBlock1_M->rtwLogInfo, "tout");
    rtliSetLogX(DeadBlock1_M->rtwLogInfo, "");
    rtliSetLogXFinal(DeadBlock1_M->rtwLogInfo, "");
    rtliSetSigLog(DeadBlock1_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(DeadBlock1_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(DeadBlock1_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(DeadBlock1_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(DeadBlock1_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &DeadBlock1_Y.Out1
      };

      rtliSetLogYSignalPtrs(DeadBlock1_M->rtwLogInfo, ((LogSignalPtrsType)
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
        "DeadBlock1/Out1" };

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

      rtliSetLogYSignalInfo(DeadBlock1_M->rtwLogInfo, rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(DeadBlock1_M->rtwLogInfo, "yout");
  }

  DeadBlock1_M->solverInfoPtr = (&DeadBlock1_M->solverInfo);
  DeadBlock1_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&DeadBlock1_M->solverInfo, 1.0);
  rtsiSetSolverMode(&DeadBlock1_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* states (dwork) */
  (void) memset((void *)&DeadBlock1_DWork, 0,
                sizeof(D_Work_DeadBlock1));

  /* external inputs */
  (void) memset((void *)&DeadBlock1_U, 0,
                sizeof(ExternalInputs_DeadBlock1));

  /* external outputs */
  DeadBlock1_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(DeadBlock1_M->rtwLogInfo, 0.0, rtmGetTFinal
    (DeadBlock1_M), DeadBlock1_M->Timing.stepSize0, (&rtmGetErrorStatus
    (DeadBlock1_M)));

  /* Initialize Sizes */
  DeadBlock1_M->Sizes.numContStates = (0);/* Number of continuous states */
  DeadBlock1_M->Sizes.numY = (1);      /* Number of model outputs */
  DeadBlock1_M->Sizes.numU = (2);      /* Number of model inputs */
  DeadBlock1_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  DeadBlock1_M->Sizes.numSampTimes = (1);/* Number of sample times */
  DeadBlock1_M->Sizes.numBlocks = (3); /* Number of blocks */
  DeadBlock1_M->Sizes.numBlockIO = (0);/* Number of block outputs */
}

/* Model terminate function */
void DeadBlock1_terminate(void)
{
}
