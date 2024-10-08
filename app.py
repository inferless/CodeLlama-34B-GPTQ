from vllm import SamplingParams, LLM

class InferlessPythonModel:
    def initialize(self):
      self.llm = LLM(model="TheBloke/CodeLlama-34B-Python-GPTQ",quantization="gptq")
    
    def infer(self, inputs):
        prompts = inputs["prompt"]
        sampling_params = SamplingParams(
            temperature=1.0,
            top_p=1,
            max_tokens=512
        )
        result = self.llm.generate(prompts, sampling_params)
        result_output = [output.outputs[0].text for output in result]

        return {"result": result_output[0]}

    def finalize(self):
        pass
