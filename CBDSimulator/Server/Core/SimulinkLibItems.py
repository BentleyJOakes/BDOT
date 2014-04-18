from Server.TCore.core.himesis import Himesis

__author__ = 'jdenil'

#TODO: Datastructures should be merged to a single one. This should be generated by scripts.

"""
Simulink blocks:
key = type
value = [[param, Simulink equivalent, type],...]
"""

CommonParameters = [
    ['BackgroundColor', 'string']
]

SimulinkBlocks = {
    'Constant':[['value','value','float'],['SampleTime', 'SampleTime', 'float']],
    'Product':[['SampleTime', 'SampleTime', 'float']],
    'Sum':[['Inputs', 'Inputs', 'string'],['SampleTime', 'SampleTime', 'float'], ['IconShape', 'IconShape', 'string']],
    'Gain':[['gain', 'gain', 'float'], ['SampleTime', 'SampleTime', 'float']],
    'UnitDelay':[['InitialCondition', 'X0', 'float'], ['SampleTime', 'SampleTime', 'float']],
    'Integrator':[['InitialCondition', 'InitialCondition','float']],
    'TransferFcn':[['Denominator', 'Denominator',  'list'], ['Numerator', 'Numerator', 'list'] ],
    'DiscreteTransferFcn':[['Denominator', 'Denominator',  'list'], ['Numerator', 'Numerator', 'list'],['SampleTime', 'SampleTime', 'float'] ],
    'DiscretePulseGenerator':[['Amplitude', 'Amplitude', 'float'],['PulseType', 'PulseType', 'string'], ['PulseWidth', 'PulseWidth', 'float'], ['Period', 'Period', 'float'], ['PhaseDelay', 'PhaseDelay', 'float']],
    'Goto': [['GotoTag', 'GotoTag', 'string'],['TagVisibility', 'TagVisibility', 'string']],
    'Derivative':[['CoefficientInTFapproximation','CoefficientInTFapproximation','float']],
    'From': [['GotoTag', 'GotoTag', 'string']],
    'Scope': [['LimitDataPoints', 'LimitDataPoints', 'string'],['NumInputPorts', 'NumInputPorts', 'string']],
    'Inport': [['Port', 'Port', 'integer']],
    'Outport': [['Port', 'Port', 'integer']],
    'DiscreteIntegrator': [['gainval', 'gainval', 'float'],['SampleTime', 'SampleTime', 'float']],
    'ZeroOrderHold':[['SampleTime', 'SampleTime', 'float']],
    'Signum':[['SampleTime', 'SampleTime', 'float']],
    'Abs':[['SampleTime', 'SampleTime', 'float']],
    'RelationalOperator':[['Operator','Operator','string'], ['SampleTime', 'SampleTime', 'float']],
    'Logic':[['Operator','Operator','string'],['SampleTime', 'SampleTime', 'float']],
    'simulink/Logic and Bit Operations/Compare To Constant':[['const','const','float'],['relop','relop', 'string']],
    'simulink/Sources/Band-Limited White Noise/White Noise':[['seed','seed','string'],['Ts','Ts', 'float'],['Cov', 'Cov', 'float']],
    '':[],

    'Pre_CommonlyUsedBlocks/Integrator':[['MT_label__','pre_label','string'],['MT_pre__InitialCondition','pre_initial','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string'], ['MT_pre__SampleTime','pre_SampleTime','string']],
    'Pre_CommonlyUsedBlocks/Gain':[['MT_label__','pre_label','string'],['MT_pre__gain','pre_gain','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'Pre_CommonlyUsedBlocks/Constant':[['MT_label__','pre_label','string'],['MT_pre__value','pre_value','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'Pre_CommonlyUsedBlocks/Unit Delay':[['MT_label__','pre_label','string'],['MT_pre__InitialCondition','pre_initial','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string'], ['MT_pre__SampleTime','pre_SampleTime','string']],
    'Pre_CommonlyUsedBlocks/Pre_InportOfBlock':[['MT_label__','pre_label','string']],
    'Pre_CommonlyUsedBlocks/Pre_OutportOfBlock':[['MT_label__','pre_label','string']],
    'Pre_CommonlyUsedBlocks/Product':[['MT_label__','pre_label','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'Pre_CommonlyUsedBlocks/Add':[['MT_label__','pre_label','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'Pre_CommonlyUsedBlocks/Transfer Fcn':[['MT_label__','pre_label','string'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string'],['MT_pre__Denominator', 'pre_Denominator',  'string'], ['MT_pre__Numerator', 'pre_Numerator', 'string']],
    'Pre_CommonlyUsedBlocks/Inport': [['MT_label__','pre_label','string'],['MT_pre__Port', 'pre_Port', 'integer'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'Pre_CommonlyUsedBlocks/Outport': [['MT_label__','pre_label','string'],['MT_pre__Port', 'pre_Port', 'integer'],['MT_pre__Name','pre_Name','string'], ['MT_pre__Position','pre_Position','string']],
    'SubSystem':[['MT_pre__Name','pre_Name','string'],['MT_post__Name','post_Name','string'],['MT_label__','p_label','string'],['MT_pre__Position','pre_Position','string'],['MT_post__Position','post_Position','string']],

    'Post_CommonlyUsedBlocks/Transfer Fcn':[['MT_label__','post_label','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string'],['MT_post__Denominator', 'post_Denominator',  'string'], ['MT_post__Numerator', 'post_Numerator', 'string']],
    'Post_CommonlyUsedBlocks/Add':[['MT_label__','post_label','string'], ['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string']],
    'Post_CommonlyUsedBlocks/Product':[['MT_label__','post_label','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string']],
    'Post_CommonlyUsedBlocks/Gain':[['MT_label__','post_label','string'], ['MT_post__gain','post_gain','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string']],
    'Post_CommonlyUsedBlocks/Constant':[['MT_label__','post_label','string'],['MT_post__value','post_value','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string']],
    'Post_CommonlyUsedBlocks/Integrator':[['MT_label__','post_label','string'],['MT_post__InitialCondition','post_initial','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string'],['MT_post__SampleTime','post_SampleTime','float']],
    'Post_CommonlyUsedBlocks/Unit Delay':[['MT_label__','post_label','string'], ['MT_post__InitialCondition','post_initial','string'],['MT_post__Name','post_Name','string'], ['MT_post__Position','post_Position','string'], ['MT_post__SampleTime','post_SampleTime','float']],
    'Post_CommonlyUsedBlocks/Post_OutportOfBlock':[['MT_label__','post_label','string']],
    'Post_CommonlyUsedBlocks/Inport': [['MT_label__','post_label','string'],['MT_post__Port', 'post_Port', 'integer'],['MT_post__Name','post_Name','string'],['MT_post__Position','post_Position','string']],
    'Post_CommonlyUsedBlocks/Outport': [['MT_label__','post_label','string'],['MT_post__Port', 'post_Port', 'integer'],['MT_post__Name','post_Name','string'],['MT_post__Position','post_Position','string'],],
    'Post_CommonlyUsedBlocks/Post_InportOfBlock':[['MT_label__','post_label','string']],
    
    'Post_CommonlyUsedBlocks/Atomic Subsystem':[['MT_post__Name','post_Name','string'],['MT_label__','p_label','string'],['MT_post__Position','post_Position','string'],['MT_post__BackgroundColor','post_BackgroundColor','string']],
'Pre_CommonlyUsedBlocks/Atomic Subsystem':[['MT_pre__Name','pre_Name','string'],['MT_label__','p_label','string'],['MT_pre__Position','pre_Position','string'],['MT_pre__BackgroundColor','pre_BackgroundColor','string']],



}

SimulinkTypes = {
    'Sum' : ["Simulink/Commonly Used Blocks/Sum",[['Inputs', 'Inputs'],['IconShape', 'IconShape']]],
    'Constant' : ["Simulink/Commonly Used Blocks/Constant", [['value','value']]],
    'Gain' : ["Simulink/Commonly Used Blocks/Gain",[['gain', 'gain']]],
    'Integrator' : ["Simulink/Commonly Used Blocks/Integrator",[['InitialCondition', 'InitialCondition']]],
    'UnitDelay' : ["Simulink/Commonly Used Blocks/Unit Delay",[['InitialCondition', 'X0'],['SampleTime', 'SampleTime']]],
    'Product' : ["Simulink/Commonly Used Blocks/Product",[]],
    'Goto':["Simulink/Signal Routing/Goto",[['GotoTag', 'GotoTag'],['TagVisibility', 'TagVisibility']]],
    'Mux':["Simulink/Commonly Used Blocks/Mux",[]],
    'Demux':["Simulink/Commonly Used Blocks/Demux",[]],
    'From':["Simulink/Signal Routing/From",[['GotoTag', 'GotoTag']]],
    'TransferFcn':["Simulink/Continuous/Transfer Fcn",[['Denominator', 'Denominator'], ['Numerator', 'Numerator']]],
    'DiscretePulseGenerator':["Simulink/Sources/Pulse Generator",[['Amplitude', 'Amplitude'],['PulseType', 'PulseType'], ['PulseWidth', 'PulseWidth'], ['Period', 'Period'], ['PhaseDelay', 'PhaseDelay']]],
    'Scope':["Simulink/Commonly Used Blocks/Scope",[['LimitDataPoints', 'LimitDataPoints'],['NumInputPorts','NumInputPorts']]],
    'SubSystem':["Simulink/Commonly Used Blocks/Subsystem",[]],
    'Outport':["Simulink/Commonly Used Blocks/Out1",[['Port', 'Port']]],
    'Inport':["Simulink/Commonly Used Blocks/In1",[['Port', 'Port']]],
    'TriggerPort':["Simulink/Ports & Subsystems/Trigger",[]]
}

TypeMapperLHS = {

    'Pre_CommonlyUsedBlocks/Integrator':'MT_pre__Integrator',
    'Pre_CommonlyUsedBlocks/Gain':'MT_pre__Gain',
    'Pre_CommonlyUsedBlocks/Constant':'MT_pre__Constant',
    'Pre_CommonlyUsedBlocks/Unit Delay':'MT_pre__UnitDelay',
    'Pre_CommonlyUsedBlocks/Pre_InportOfBlock':'MT_pre__Port_Output',
    'Pre_CommonlyUsedBlocks/Pre_OutportOfBlock':'MT_pre__Port_Input',
    'Pre_CommonlyUsedBlocks/Product':'MT_pre__Product',
    'Pre_CommonlyUsedBlocks/Add':'MT_pre__Sum',
    'Pre_CommonlyUsedBlocks/Transfer Fcn':'MT_pre__TransferFcn',
    'Pre_CommonlyUsedBlocks/Atomic Subsystem': 'MT_pre_SubSystem',
    'Pre_CommonlyUsedBlocks/Inport':'MT_pre__Inport',
    'Pre_CommonlyUsedBlocks/Outport':'MT_pre__Outport',
    'Port_Output':'MT_pre__Port_Output',
    'Port_Input':'MT_pre__Port_Input',
    'SubSystem': 'MT_pre__SubSystem',
    'MT_pre____Contains__':'MT_pre____Contains__'
}

TypeMapperRHs = {
    'Post_CommonlyUsedBlocks/Add':'MT_post__Sum',
    'Post_CommonlyUsedBlocks/Product':'MT_post__Product',
    'Post_CommonlyUsedBlocks/Gain':'MT_post__Gain',
    'Post_CommonlyUsedBlocks/Constant':'MT_post__Constant',
    'Post_CommonlyUsedBlocks/Integrator':'MT_post__Integrator',
    'Post_CommonlyUsedBlocks/Unit Delay':'MT_post__UnitDelay',
    'Post_CommonlyUsedBlocks/Post_OutportOfBlock':'MT_post__Port_Input',
    'Post_CommonlyUsedBlocks/Post_InportOfBlock':'MT_post__Port_Output',
    'Post_CommonlyUsedBlocks/Transfer Fcn':'MT_post__TransferFcn',
    'Post_CommonlyUsedBlocks/Atomic Subsystem': 'MT_post_SubSystem',
    'Post_CommonlyUsedBlocks/Inport':'MT_post__Inport',
    'Post_CommonlyUsedBlocks/Outport':'MT_post__Outport',
    'Port_Output':'MT_post__Port_Output',
    'Port_Input':'MT_post__Port_Input',
    'SubSystem':'MT_post__SubSystem',
    'MT_post____Contains__':'MT_post____Contains__'
}

AbstractBlockSubTypes = ['Constant',
                         'Product',
                         'Sum',
                         'Gain',
                         'UnitDelay',
                         'Integrator',
                         'TransferFcn',
                         'DiscreteTransferFcn',
                         'DiscretePulseGenerator',
                         'Goto',
                         'Derivative',
                         'From',
                         'Scope',
                         'Outport',
                         'Inport',
                         'DiscreteIntegrator',
                         'ZeroOrderHold',
                         'Signum',
                         'Abs',
                         'RelationalOperator',
                         'Logic',
                         'DataStoreMemory',
                         'DataStoreRead',
                         'DataStoreWrite'
]


def getPreSubTypes():
    rv = []
    for block in AbstractBlockSubTypes:
        rv.append(Himesis.Constants.MT_PRECOND_PREFIX+block)
    return rv

class S2HConstants:
    BLOCK_INPORT_RELATION = '__Block_Inport__'
    BLOCK_OUTPORT_RELATION = '__Block_Outport__'
    BLOCK_TRIGGER_RELATION = '__Block_Trigger__'
    BLOCK_ENABLE_RELATION = '__Block_Enable__'

    PORT2PORT_RELATION = '__Relation__'
    CONTAINMENT_RELATION = '__Contains__'
