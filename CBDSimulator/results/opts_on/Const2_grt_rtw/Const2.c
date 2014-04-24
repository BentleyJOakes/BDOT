/*
 * Const2.c
 *
 * Code generation for model "Const2".
 *
 * Model version              : 1.7
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:16:47 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#include "Const2.h"
#include "Const2_private.h"

/* External outputs (root outports fed by signals with auto storage) */
ExternalOutputs_Const2 Const2_Y;

/* Real-time model */
RT_MODEL_Const2 Const2_M_;
RT_MODEL_Const2 *const Const2_M = &Const2_M_;

/* Model step function */
void Const2_step(void)
{
  /* Matfile logging */
  rt_UpdateTXYLogVars(Const2_M->rtwLogInfo, (Const2_M->Timing.t));

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++Const2_M->Timing.clockTick0)) {
    ++Const2_M->Timing.clockTickH0;
  }

  Const2_M->Timing.t[0] = Const2_M->Timing.clockTick0 *
    Const2_M->Timing.stepSize0 + Const2_M->Timing.clockTickH0 *
    Const2_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void Const2_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)Const2_M, 0,
                sizeof(RT_MODEL_Const2));

  /* Initialize timing info */
  {
    int_T *mdlTsMap = Const2_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    Const2_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    Const2_M->Timing.sampleTimes = (&Const2_M->Timing.sampleTimesArray[0]);
    Const2_M->Timing.offsetTimes = (&Const2_M->Timing.offsetTimesArray[0]);

    /* task periods */
    Const2_M->Timing.sampleTimes[0] = (1.0);

    /* task offsets */
    Const2_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(Const2_M, &Const2_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = Const2_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    Const2_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(Const2_M, 1.0E+8);
  Const2_M->Timing.stepSize0 = 1.0;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    Const2_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(Const2_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(Const2_M->rtwLogInfo, (NULL));
    rtliSetLogT(Const2_M->rtwLogInfo, "tout");
    rtliSetLogX(Const2_M->rtwLogInfo, "");
    rtliSetLogXFinal(Const2_M->rtwLogInfo, "");
    rtliSetSigLog(Const2_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(Const2_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(Const2_M->rtwLogInfo, 0);
    rtliSetLogMaxRows(Const2_M->rtwLogInfo, 1000);
    rtliSetLogDecimation(Const2_M->rtwLogInfo, 1);

    /*
     * Set pointers to the data and signal info for each output
     */
    {
      static void * rt_LoggedOutputSignalPtrs[] = {
        &Const2_Y.Out1
      };

      rtliSetLogYSignalPtrs(Const2_M->rtwLogInfo, ((LogSignalPtrsType)
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
        "Const2/Out1" };

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

      rtliSetLogYSignalInfo(Const2_M->rtwLogInfo, rt_LoggedOutputSignalInfo);

      /* set currSigDims field */
      rt_LoggedCurrentSignalDimensions[0] = &rt_LoggedOutputWidths[0];
    }

    rtliSetLogY(Const2_M->rtwLogInfo, "yout");
  }

  Const2_M->solverInfoPtr = (&Const2_M->solverInfo);
  Const2_M->Timing.stepSize = (1.0);
  rtsiSetFixedStepSize(&Const2_M->solverInfo, 1.0);
  rtsiSetSolverMode(&Const2_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* external outputs */
  Const2_Y.Out1 = 0.0;

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(Const2_M->rtwLogInfo, 0.0, rtmGetTFinal
    (Const2_M), Const2_M->Timing.stepSize0, (&rtmGetErrorStatus(Const2_M)));

  /* Initialize Sizes */
  Const2_M->Sizes.numContStates = (0); /* Number of continuous states */
  Const2_M->Sizes.numY = (1);          /* Number of model outputs */
  Const2_M->Sizes.numU = (0);          /* Number of model inputs */
  Const2_M->Sizes.sysDirFeedThru = (0);/* The model is not direct feedthrough */
  Const2_M->Sizes.numSampTimes = (1);  /* Number of sample times */
  Const2_M->Sizes.numBlocks = (4);     /* Number of blocks */
  Const2_M->Sizes.numBlockIO = (0);    /* Number of block outputs */

  /* ConstCode for Outport: '<Root>/Out1' */
  Const2_Y.Out1 = 249.0;
}

/* Model terminate function */
void Const2_terminate(void)
{
}
