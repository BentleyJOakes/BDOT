/*
 * Const1_export.c
 *
 * Code generation for model "Const1_export".
 *
 * Model version              : 1.4
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:29:23 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "Const1_export.h"
#include "Const1_export_private.h"

/* External inputs (root inport signals with auto storage) */
ExternalInputs_Const1_export Const1_export_U;

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_Const1_export Const1_export_Y;

/* Real-time model */
RT_MODEL_Const1_export Const1_export_M_;
RT_MODEL_Const1_export *const Const1_export_M = &Const1_export_M_;

/* Model step function */
void Const1_export_step(void)
{
  /* Outport: '<Root>/Out1' incorporates:
   *  Constant: '<Root>/Constant23'
   *  Inport: '<Root>/In1'
   *  Sum: '<Root>/Sum'
   */
  Const1_export_Y.Out1 = Const1_export_U.In1 + 439.304;

  /* Matfile logging */
  rt_UpdateTXYLogVars(Const1_export_M->rtwLogInfo, (Const1_export_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++Const1_export_M->Timing.clockTick0)) {
    ++Const1_export_M->Timing.clockTickH0;
  }

  Const1_export_M->Timing.t[0] = Const1_export_M->Timing.clockTick0 *
    Const1_export_M->Timing.stepSize0 + Const1_export_M->Timing.clockTickH0 *
    Const1_export_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void Const1_export_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)Const1_export_M, 0,
                sizeof(RT_MODEL_Const1_export));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = Const1_export_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    Const1_export_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    Const1_export_M->Timing.sampleTimes =
      (&Const1_export_M->Timing.sampleTimesArray[0]);
    Const1_export_M->Timing.offsetTimes =
      (&Const1_export_M->Timing.offsetTimesArray[0]);

    /* task periods */
    Const1_export_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    Const1_export_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(Const1_export_M, &Const1_export_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = Const1_export_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    Const1_export_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(Const1_export_M, 1.0E+8);
  Const1_export_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    Const1_export_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(Const1_export_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(Const1_export_M->rtwLogInfo, (NULL));
    rtliSetLogT(Const1_export_M->rtwLogInfo, "tout");
    rtliSetLogX(Const1_export_M->rtwLogInfo, "");
    rtliSetLogXFinal(Const1_export_M->rtwLogInfo, "");
    rtliSetSigLog(Const1_export_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(Const1_export_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(Const1_export_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(Const1_export_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(Const1_export_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &Const1_export_Y.Out1
      };

      rtliSetLogYSignalPtrs(Const1_export_M->rtwLogInfo, ((LogSignalPtrsType)
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
        "Const1_export/Out1" };

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

      rtliSetLogYSignalInfo(Const1_export_M->rtwLogInfo,
                            rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(Const1_export_M->rtwLogInfo, "yout");
  }

  Const1_export_M->solverInfoPtr = (&Const1_export_M->solverInfo);
  Const1_export_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&Const1_export_M->solverInfo, 1.0);
  rtsiSetSolverMode(&Const1_export_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* external inputs */
  Const1_export_U.In1 = 0.0;

  /* external outputs */
  Const1_export_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(Const1_export_M->rtwLogInfo, 0.0,
    rtmGetTFinal(Const1_export_M), Const1_export_M->Timing.stepSize0,
    (&rtmGetErrorStatus(Const1_export_M)));

  /* Initialize Sizes */
  Const1_export_M->Sizes.numContStates = (0);/* Number of continuous states */
  Const1_export_M->Sizes.numY = (1);   /* Number of model outputs */
  Const1_export_M->Sizes.numU = (1);   /* Number of model inputs */
  Const1_export_M->Sizes.sysDirFeedThru = (1);/* The model is direct feedthrough */
  Const1_export_M->Sizes.numSampTimes = (1);/* Number of sample times */
  Const1_export_M->Sizes.numBlocks = (3);/* Number of blocks */
  Const1_export_M->Sizes.numBlockIO = (0);/* Number of block outputs */
}

/* Model terminate function */
void Const1_export_terminate(void)
{
}
