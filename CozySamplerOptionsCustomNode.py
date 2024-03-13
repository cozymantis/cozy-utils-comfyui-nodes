import comfy.samplers

class CozySamplerOptionsCustomNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                  {
                    "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                    "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01}),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step":0.01, "round": 0.01}),
                  }
                }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "INT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("sampler_name", "scheduler_name", "steps", "cfg", "denoise")
    FUNCTION = "run"
    CATEGORY = "CozyMantis"

    def run(self, sampler_name, scheduler, steps, cfg, denoise):
        return (sampler_name, scheduler, steps, cfg, denoise)