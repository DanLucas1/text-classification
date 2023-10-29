from skllm.config import SKLLMConfig

key = input('enter openAI key:\n')

SKLLMConfig.set_openai_key(f'{key}')
SKLLMConfig.set_openai_org("org-lFhItV8DbQoI0lkfgqpxnrLm")
print('ran setup.py')
