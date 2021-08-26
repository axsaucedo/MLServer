"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

#
# ServerLive messages.
class ServerLiveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ServerLiveRequest = ServerLiveRequest

class ServerLiveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIVE_FIELD_NUMBER: builtins.int
    # True if the inference server is live, false if not live.
    live: builtins.bool = ...
    def __init__(self,
        *,
        live : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"live",b"live"]) -> None: ...
global___ServerLiveResponse = ServerLiveResponse

#
# ServerReady messages.
class ServerReadyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ServerReadyRequest = ServerReadyRequest

class ServerReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READY_FIELD_NUMBER: builtins.int
    # True if the inference server is ready, false if not ready.
    ready: builtins.bool = ...
    def __init__(self,
        *,
        ready : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ready",b"ready"]) -> None: ...
global___ServerReadyResponse = ServerReadyResponse

#
# ModelReady messages.
class ModelReadyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    # The name of the model to check for readiness.
    name: typing.Text = ...
    # The version of the model to check for readiness. If not given the
    # server will choose a version based on the model and internal policy.
    version: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"version",b"version"]) -> None: ...
global___ModelReadyRequest = ModelReadyRequest

class ModelReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READY_FIELD_NUMBER: builtins.int
    # True if the model is ready, false if not ready.
    ready: builtins.bool = ...
    def __init__(self,
        *,
        ready : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ready",b"ready"]) -> None: ...
global___ModelReadyResponse = ModelReadyResponse

#
# ServerMetadata messages.
class ServerMetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ServerMetadataRequest = ServerMetadataRequest

class ServerMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    EXTENSIONS_FIELD_NUMBER: builtins.int
    # The server name.
    name: typing.Text = ...
    # The server version.
    version: typing.Text = ...
    # The extensions supported by the server.
    @property
    def extensions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        version : typing.Text = ...,
        extensions : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"extensions",b"extensions",u"name",b"name",u"version",b"version"]) -> None: ...
global___ServerMetadataResponse = ServerMetadataResponse

#
# ModelMetadata messages.
class ModelMetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    # The name of the model.
    name: typing.Text = ...
    # The version of the model to check for readiness. If not given the
    # server will choose a version based on the model and internal policy.
    version: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"version",b"version"]) -> None: ...
global___ModelMetadataRequest = ModelMetadataRequest

class ModelMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # Metadata for a tensor.
    class TensorMetadata(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class TagsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___InferParameter] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        TAGS_FIELD_NUMBER: builtins.int
        # The tensor name.
        name: typing.Text = ...
        # The tensor data type.
        datatype: typing.Text = ...
        # The tensor shape. A variable-size dimension is represented
        # by a -1 value.
        @property
        def shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        # Optional tags about the input.
        # NOTE: This is an extension to the standard
        @property
        def tags(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
        def __init__(self,
            *,
            name : typing.Text = ...,
            datatype : typing.Text = ...,
            shape : typing.Optional[typing.Iterable[builtins.int]] = ...,
            tags : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"datatype",b"datatype",u"name",b"name",u"shape",b"shape",u"tags",b"tags"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    VERSIONS_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    # The model name.
    name: typing.Text = ...
    # The versions of the model available on the server.
    @property
    def versions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    # The model's platform. See Platforms.
    platform: typing.Text = ...
    # The model's inputs.
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelMetadataResponse.TensorMetadata]: ...
    # The model's outputs.
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelMetadataResponse.TensorMetadata]: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        versions : typing.Optional[typing.Iterable[typing.Text]] = ...,
        platform : typing.Text = ...,
        inputs : typing.Optional[typing.Iterable[global___ModelMetadataResponse.TensorMetadata]] = ...,
        outputs : typing.Optional[typing.Iterable[global___ModelMetadataResponse.TensorMetadata]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"inputs",b"inputs",u"name",b"name",u"outputs",b"outputs",u"platform",b"platform",u"versions",b"versions"]) -> None: ...
global___ModelMetadataResponse = ModelMetadataResponse

#
# ModelInfer messages.
class ModelInferRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # An input tensor for an inference request.
    class InferInputTensor(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___InferParameter] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        CONTENTS_FIELD_NUMBER: builtins.int
        # The tensor name.
        name: typing.Text = ...
        # The tensor data type.
        datatype: typing.Text = ...
        # The tensor shape.
        @property
        def shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        # Optional inference input tensor parameters.
        @property
        def parameters(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
        # The input tensor data.
        @property
        def contents(self) -> global___InferTensorContents: ...
        def __init__(self,
            *,
            name : typing.Text = ...,
            datatype : typing.Text = ...,
            shape : typing.Optional[typing.Iterable[builtins.int]] = ...,
            parameters : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
            contents : typing.Optional[global___InferTensorContents] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"contents",b"contents"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"contents",b"contents",u"datatype",b"datatype",u"name",b"name",u"parameters",b"parameters",u"shape",b"shape"]) -> None: ...

    # An output tensor requested for an inference request.
    class InferRequestedOutputTensor(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___InferParameter] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        # The tensor name.
        name: typing.Text = ...
        # Optional requested output tensor parameters.
        @property
        def parameters(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
        def __init__(self,
            *,
            name : typing.Text = ...,
            parameters : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"parameters",b"parameters"]) -> None: ...

    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___InferParameter: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    MODEL_NAME_FIELD_NUMBER: builtins.int
    MODEL_VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    # The name of the model to use for inferencing.
    model_name: typing.Text = ...
    # The version of the model to use for inference. If not given the
    # server will choose a version based on the model and internal policy.
    model_version: typing.Text = ...
    # Optional identifier for the request. If specified will be
    # returned in the response.
    id: typing.Text = ...
    # Optional inference parameters.
    @property
    def parameters(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
    # The input tensors for the inference.
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelInferRequest.InferInputTensor]: ...
    # The requested output tensors for the inference. Optional, if not
    # specified all outputs produced by the model will be returned.
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelInferRequest.InferRequestedOutputTensor]: ...
    def __init__(self,
        *,
        model_name : typing.Text = ...,
        model_version : typing.Text = ...,
        id : typing.Text = ...,
        parameters : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
        inputs : typing.Optional[typing.Iterable[global___ModelInferRequest.InferInputTensor]] = ...,
        outputs : typing.Optional[typing.Iterable[global___ModelInferRequest.InferRequestedOutputTensor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id",u"inputs",b"inputs",u"model_name",b"model_name",u"model_version",b"model_version",u"outputs",b"outputs",u"parameters",b"parameters"]) -> None: ...
global___ModelInferRequest = ModelInferRequest

class ModelInferResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # An output tensor returned for an inference request.
    class InferOutputTensor(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[global___InferParameter] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        CONTENTS_FIELD_NUMBER: builtins.int
        # The tensor name.
        name: typing.Text = ...
        # The tensor data type.
        datatype: typing.Text = ...
        # The tensor shape.
        @property
        def shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        # Optional output tensor parameters.
        @property
        def parameters(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
        # The output tensor data.
        @property
        def contents(self) -> global___InferTensorContents: ...
        def __init__(self,
            *,
            name : typing.Text = ...,
            datatype : typing.Text = ...,
            shape : typing.Optional[typing.Iterable[builtins.int]] = ...,
            parameters : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
            contents : typing.Optional[global___InferTensorContents] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"contents",b"contents"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"contents",b"contents",u"datatype",b"datatype",u"name",b"name",u"parameters",b"parameters",u"shape",b"shape"]) -> None: ...

    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___InferParameter: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    MODEL_NAME_FIELD_NUMBER: builtins.int
    MODEL_VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    # The name of the model used for inference.
    model_name: typing.Text = ...
    # The version of the model used for inference.
    model_version: typing.Text = ...
    # The id of the inference request if one was specified.
    id: typing.Text = ...
    # Optional inference response parameters.
    @property
    def parameters(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___InferParameter]: ...
    # The output tensors holding inference results.
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModelInferResponse.InferOutputTensor]: ...
    def __init__(self,
        *,
        model_name : typing.Text = ...,
        model_version : typing.Text = ...,
        id : typing.Text = ...,
        parameters : typing.Optional[typing.Mapping[typing.Text, global___InferParameter]] = ...,
        outputs : typing.Optional[typing.Iterable[global___ModelInferResponse.InferOutputTensor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id",u"model_name",b"model_name",u"model_version",b"model_version",u"outputs",b"outputs",u"parameters",b"parameters"]) -> None: ...
global___ModelInferResponse = ModelInferResponse

#
# An inference parameter value.
class InferParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOOL_PARAM_FIELD_NUMBER: builtins.int
    INT64_PARAM_FIELD_NUMBER: builtins.int
    STRING_PARAM_FIELD_NUMBER: builtins.int
    # A boolean parameter value.
    bool_param: builtins.bool = ...
    # An int64 parameter value.
    int64_param: builtins.int = ...
    # A string parameter value.
    string_param: typing.Text = ...
    def __init__(self,
        *,
        bool_param : builtins.bool = ...,
        int64_param : builtins.int = ...,
        string_param : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bool_param",b"bool_param",u"int64_param",b"int64_param",u"parameter_choice",b"parameter_choice",u"string_param",b"string_param"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bool_param",b"bool_param",u"int64_param",b"int64_param",u"parameter_choice",b"parameter_choice",u"string_param",b"string_param"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"parameter_choice",b"parameter_choice"]) -> typing.Optional[typing_extensions.Literal["bool_param","int64_param","string_param"]]: ...
global___InferParameter = InferParameter

#
# The data contained in a tensor. For a given data type the
# tensor contents can be represented in "raw" bytes form or in
# the repeated type that matches the tensor's data type. Protobuf
# oneof is not used because oneofs cannot contain repeated fields.
class InferTensorContents(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOOL_CONTENTS_FIELD_NUMBER: builtins.int
    INT_CONTENTS_FIELD_NUMBER: builtins.int
    INT64_CONTENTS_FIELD_NUMBER: builtins.int
    UINT_CONTENTS_FIELD_NUMBER: builtins.int
    UINT64_CONTENTS_FIELD_NUMBER: builtins.int
    FP32_CONTENTS_FIELD_NUMBER: builtins.int
    FP64_CONTENTS_FIELD_NUMBER: builtins.int
    BYTES_CONTENTS_FIELD_NUMBER: builtins.int
    # Representation for BOOL data type. The size must match what is
    # expected by the tensor's shape. The contents must be the flattened,
    # one-dimensional, row-major order of the tensor elements.
    @property
    def bool_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    # Representation for INT8, INT16, and INT32 data types. The size
    # must match what is expected by the tensor's shape. The contents
    # must be the flattened, one-dimensional, row-major order of the
    # tensor elements.
    @property
    def int_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Representation for INT64 data types. The size must match what
    # is expected by the tensor's shape. The contents must be the
    # flattened, one-dimensional, row-major order of the tensor elements.
    @property
    def int64_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Representation for UINT8, UINT16, and UINT32 data types. The size
    # must match what is expected by the tensor's shape. The contents
    # must be the flattened, one-dimensional, row-major order of the
    # tensor elements.
    @property
    def uint_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Representation for UINT64 data types. The size must match what
    # is expected by the tensor's shape. The contents must be the
    # flattened, one-dimensional, row-major order of the tensor elements.
    @property
    def uint64_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Representation for FP32 data type. The size must match what is
    # expected by the tensor's shape. The contents must be the flattened,
    # one-dimensional, row-major order of the tensor elements.
    @property
    def fp32_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    # Representation for FP64 data type. The size must match what is
    # expected by the tensor's shape. The contents must be the flattened,
    # one-dimensional, row-major order of the tensor elements.
    @property
    def fp64_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    # Representation for BYTES data type. The size must match what is
    # expected by the tensor's shape. The contents must be the flattened,
    # one-dimensional, row-major order of the tensor elements.
    @property
    def bytes_contents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        bool_contents : typing.Optional[typing.Iterable[builtins.bool]] = ...,
        int_contents : typing.Optional[typing.Iterable[builtins.int]] = ...,
        int64_contents : typing.Optional[typing.Iterable[builtins.int]] = ...,
        uint_contents : typing.Optional[typing.Iterable[builtins.int]] = ...,
        uint64_contents : typing.Optional[typing.Iterable[builtins.int]] = ...,
        fp32_contents : typing.Optional[typing.Iterable[builtins.float]] = ...,
        fp64_contents : typing.Optional[typing.Iterable[builtins.float]] = ...,
        bytes_contents : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bool_contents",b"bool_contents",u"bytes_contents",b"bytes_contents",u"fp32_contents",b"fp32_contents",u"fp64_contents",b"fp64_contents",u"int64_contents",b"int64_contents",u"int_contents",b"int_contents",u"uint64_contents",b"uint64_contents",u"uint_contents",b"uint_contents"]) -> None: ...
global___InferTensorContents = InferTensorContents
