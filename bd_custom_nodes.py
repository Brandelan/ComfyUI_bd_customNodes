"""
@author: Brandelan
@title: bd Nodes
@nickname: bd Nodes
@description: This extension offers various custom nodes for some randomization and QOL.
"""

import math
import random
import re

EPSILON = 0.00001

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class StaticLibrary:
    def almostEqual(a: float, b: float):
        if (abs(a - b) > EPSILON) :
            return False        
        return True

   

class bd_RandomRange:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "min": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "max": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
        }

    RETURN_TYPES = ("FLOAT", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "getRandomRange"
    OUTPUT_NODE = True
    CATEGORY = "bd Nodes"

    @staticmethod
    def getRandomRange(min, max, seed):
        random.seed(seed)
        outFloat = random.uniform(min, max)
        outInt = math.floor(outFloat)

        print(f"random number is {outFloat}")

        #output = str(outFloat)

        return outFloat, outInt
    

class bd_Settings:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "cfg": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "steps": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "denoise": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                "variation_amount": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "refiner_amount": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
            "optional":{                
                "control_net_strength": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  1.0, "step": 0.01, "display": "number"}),
                "custom_01": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "custom_02": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "custom_03": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
            }
            # "hidden":{
            #     "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            # }
        }

    RETURN_TYPES = ("FLOAT", "INT", "FLOAT", "INT", "INT", "FLOAT", "FLOAT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("cfg", "steps", "denoise", "refiner start", "var seed", "controlnet strength", "custom 01", "custom 02", "custom 03")
    FUNCTION = "randomize_it"
    OUTPUT_NODE = True
    CATEGORY = "bd Nodes"

    @staticmethod
    def randomize(base : float, variation_amount: float) -> float: 
        #get a random number in the range of [-1, 1], then reduce by our variation amount
        rbase = random.random()
        rbase = rbase * 2.0 - 1.0
        rbase *= variation_amount

        outval = base + (base * rbase)

        return outval
    
    @staticmethod
    def clamp(n : float|int, min: float|int, max: float|int) -> float|int:
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
        

    @staticmethod
    def calc_refiner(steps: int, refiner_amt: float):
        refiner_start = steps - math.floor(float(steps) * refiner_amt)
        return refiner_start
    
    @staticmethod
    def randomize_it(cfg, steps, variation_amount, denoise, seed, refiner_amount, control_net_strength, custom_01, custom_02, custom_03):

        #exit early  and just return the settings
        if StaticLibrary.almostEqual(variation_amount, 0):
            refiner_start = bd_Settings.calc_refiner(steps, refiner_amount)
            print(f"bd settings: no variation amount supplied, using supplied values seed is {seed} cfg is {cfg} and random step amount is {steps}, denoise amt is {denoise}, refiner start is {refiner_start}, custom00 is {custom_00}, custom_01 is {custom_01}, custom_02 is {custom_02}, custom_03 is {custom_03}")
            return (cfg, steps, denoise, refiner_start, seed, control_net_strength, custom_01, custom_02, custom_03)
        
        
        #set our new seed
        random.seed(seed)

        outcfg = bd_Settings.randomize(cfg, variation_amount)
        outcfg = round(outcfg, 2) # make the cfg a bit more simple
        outsteps = math.floor(bd_Settings.randomize(float(steps), variation_amount))
        outdenoise = bd_Settings.randomize(denoise, variation_amount)
        outdenoise = bd_Settings.clamp(outdenoise, 0.0, 1.0)        
        refiner_start = bd_Settings.calc_refiner(outsteps, refiner_amount)

        out_custom00 = bd_Settings.randomize(control_net_strength, variation_amount)
        out_custom01 = bd_Settings.randomize(custom_01, variation_amount)
        out_custom02 = bd_Settings.randomize(custom_02, variation_amount)
        out_custom03 = bd_Settings.randomize(custom_03, variation_amount)


        print(f"bd settings: for variation amount {variation_amount} seed is {seed} cfg is {outcfg} and random step amount is {outsteps}, denoise amt is {outdenoise}, refiner start is {refiner_start}, custom00 is {out_custom00}, custom01 is {out_custom01}, custom02 is {out_custom02}, custom03 is {out_custom03}")

        #output = str(outFloat)

        return outcfg, outsteps, outdenoise, refiner_start, seed, out_custom00, out_custom01, out_custom02, out_custom03
    


class bd_SettingsDraft:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "mode": (["standard", "draft (no variations)", "standard (no variations)", "draft (with variations)"], {"default": "standard"}),
                "cfg": ("FLOAT", {"default": 6.0, "min": 0.0, "max": 0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "steps": ("INT", {"default": 30, "min": 0, "max": 0xffffffffffffffff}),
                "variation_amount": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "refiner_amount": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                "aspect_ratio": (
                    ["1:1 Square (1024x1024)", 
                     "7:4 Widescreen (1344x768)", 
                     "13:19 Portrait (832x1216)", 
                     "12:15 Wide Landscape (1536x640)",
                     ], {"default": "1:1 Square (1024x1024)"}
                     ),                
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
            "optional":{
                "custom_00": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  1.0, "step": 0.01, "display": "number"}),
                "custom_01": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "custom_02": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
                "custom_03": ("FLOAT", {"default": 0.1, "min": 0.0, "max":  0xffffffffffffffff, "step": 0.01, "display": "number"}),
            }
            # "hidden":{
            #     "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            # }
        }

    RETURN_TYPES = ("FLOAT", "INT", "INT", "INT", "INT", "INT", "FLOAT", "FLOAT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("cfg", "steps", "refiner start", "width", "height", "var seed", "custom 00", "custom 01", "custom 02", "custom 03")
    FUNCTION = "randomize_it"
    OUTPUT_NODE = True
    CATEGORY = "bd Nodes"

    @staticmethod
    def randomize(base : float, variation_amount: float) -> float: 
        #get a random number in the range of [-1, 1], then reduce by our variation amount
        rbase = random.random()
        rbase = rbase * 2.0 - 1.0
        rbase *= variation_amount

        outval = base + (base * rbase)

        return outval
    
    @staticmethod
    def clamp(n : float|int, min: float|int, max: float|int) -> float|int:
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
        

    @staticmethod
    def calc_refiner(steps: int, refiner_amt: float):
        refiner_start = steps - math.floor(float(steps) * refiner_amt)
        return refiner_start
    
    @staticmethod
    def randomize_it(mode, cfg, steps, variation_amount, seed, refiner_amount, custom_00, custom_01, custom_02, custom_03, aspect_ratio):

        draft_amt = .3333
        width = 1024
        height = 1024

        if(aspect_ratio == "1:1 Square (1024x1024)"):
            width = 1024
            height = 1024
        if(aspect_ratio == "7:4 Widescreen (1344x768)"):
            width = 1344
            height = 768
        if(aspect_ratio == "13:19 Portrait (832x1216)"):
            width = 832
            height = 1216
        if(aspect_ratio == "12:15 Wide Landscape (1536x640)"):
            width = 1536
            height = 640

        #if in draft mode, significantly lower the steps amount and remove variation. The point of draft mode is rapid iteration that we can then go back and add variation to
        if(mode == "draft (with variations)"):
            steps = math.floor(float(steps) * draft_amt)
            steps = steps if steps > 0 else  1
            print(f"Working in draft mode with variations, steps reduced to {steps}")

        elif(mode == "draft (no variations)"):
            steps = math.floor(float(steps) * draft_amt)
            steps = steps if steps > 0 else  1
            variation_amount = 0.0
            print(f"Working in draft mode, ignoring variations, steps reduced to {steps}, and variation amount reduced to {variation_amount}")

        elif(mode == "standard (no variations)"):
            variation_amount = 0.0
            print(f"Working in standard no variations mode, variation amount reduced to {variation_amount}")

        #exit early  and just return the settings
        if StaticLibrary.almostEqual(variation_amount, 0):
            refiner_start = bd_Settings.calc_refiner(steps, refiner_amount)
            print(f"{bcolors.OKCYAN}bd settings:{bcolors.ENDC}\n" +
                  f"no variation amount supplied, using supplied values.\n" + 
                  f"seed is {seed}, cfg is {cfg}, random step amount is {steps}, refiner start is {refiner_start},\n" + 
                  f"custom00 is {custom_00}, custom_01 is {custom_01}, custom_02 is {custom_02}, custom_03 is {custom_03}, width is {width}, height is {height}")
            return (cfg, steps, refiner_start, width, height, seed, custom_00, custom_01, custom_02, custom_03)
        
        
        #set our new seed
        random.seed(seed)

        outcfg = bd_Settings.randomize(cfg, variation_amount)
        outcfg = round(outcfg, 2) # make the cfg a bit more simple
        outsteps = math.floor(bd_Settings.randomize(float(steps), variation_amount))
 
        refiner_start = bd_Settings.calc_refiner(outsteps, refiner_amount)

        out_custom00 = bd_Settings.randomize(custom_00, variation_amount)
        out_custom01 = bd_Settings.randomize(custom_01, variation_amount)
        out_custom02 = bd_Settings.randomize(custom_02, variation_amount)
        out_custom03 = bd_Settings.randomize(custom_03, variation_amount)


        print(f"{bcolors.OKCYAN}bd settings:{bcolors.ENDC}\n" +
              f"for variation amount {variation_amount}:\n" + 
              f"seed is {seed}, cfg is {outcfg}, random step amount is {outsteps}, refiner start is {refiner_start},\n" + 
              f"custom00 is {out_custom00}, custom_01 is {custom_01}, custom_02 is {out_custom02}, custom_03 is {out_custom03}, width is {width}, height is {height}")

        return outcfg, outsteps,  refiner_start, width, height, seed, out_custom00, out_custom01, out_custom02, out_custom03
    



class bd_txt2img:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "steps": ("INT", {"default": 30, "min": 0, "max": 0xffffffffffffffff}),
                "txt2img": ("LATENT",),
                "img2img": ("LATENT",),                
                "txt2img_switch": (
                    ["txt2img", "img2img"], {"default": "txt2img"}
                )
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
            "optional":{                
                "img2img_strength": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
            }
            # "hidden":{
            #     "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            # }
        }

    RETURN_TYPES = ("INT", "LATENT")
    RETURN_NAMES = ("start at step", "LATENT")
    FUNCTION = "randomize_it"
    OUTPUT_NODE = True
    CATEGORY = "bd Nodes"

    @staticmethod
    def randomize(base : float, variation_amount: float) -> float: 
        #get a random number in the range of [-1, 1], then reduce by our variation amount
        rbase = random.random()
        rbase = rbase * 2.0 - 1.0
        rbase *= variation_amount

        outval = base + (base * rbase)

        return outval
    
    @staticmethod
    def clamp(n : float|int, min: float|int, max: float|int) -> float|int:
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
        

    @staticmethod
    def calc_refiner(steps: int, refiner_amt: float):
        refiner_start = steps - math.floor(float(steps) * refiner_amt)
        return refiner_start
    
    @staticmethod
    def randomize_it(steps, img2img_strength, txt2img_switch, txt2img, img2img):

        
        outLatent = txt2img
        if(txt2img_switch == "img2img"):
            outLatent = img2img        

        out_start_step = math.floor(float(steps) * img2img_strength)

        print(f"{bcolors.OKCYAN}bd settings:{bcolors.ENDC}\n" +
              f" base start step is {out_start_step}" )

        return  out_start_step, outLatent
    
class bd_Sequencer:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):      
        self.reg = r"[\d]+"
        self.step = 0
        self.seed = 0
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "steps": ("STRING", {
                "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                "default": "0"
                }),     
                "randomize_after_sequence": (["enable", "disable"],),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),

            },
        }

    RETURN_TYPES = ("FLOAT", "INT", "INT")
    RETURN_NAMES = ("float", "int", "seed")
    FUNCTION = "sequence_it"
    OUTPUT_NODE = True
    CATEGORY = "bd Nodes"

    @staticmethod
    def randomize(base : float, variation_amount: float) -> float: 
        #get a random number in the range of [-1, 1], then reduce by our variation amount
        rbase = random.random()
        rbase = rbase * 2.0 - 1.0
        rbase *= variation_amount

        outval = base + (base * rbase)

        return outval
    
    @staticmethod
    def clamp(n : float|int, min: float|int, max: float|int) -> float|int:
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
    
    
    def sequence_it(self, steps, seed, randomize_after_sequence):

        if(self.step == 0):
            #set our new seed
            self.seed = seed
            random.seed(self.seed)

        
        #if we want a random seed after each step, make sure to update self.seed
        if(randomize_after_sequence == "disable"):
            self.seed = seed

        matches = re.findall(self.reg, steps)

        print(f'expression is {self.reg}, seed is {seed}, self.seed is {self.seed}, steps are {steps} matches are {matches}')

        if(matches == None or len(matches) == 0):
            print(f"Check that your steps are set to the correct format, only numbers and separators")
            return ("NaN", "NaN")


        counter = 0
        for gr in matches:
                print(f"self.step is {self.step} and gr is {gr}")
                if(self.step == counter):
                    self.step += 1
                    #loop back around to start
                    self.step %= len(matches)
                    print(f"self.step in loop is {self.step}")
                    print(f"sequencer output is {gr}")
                    return (float(gr), int(gr), self.seed)
  
                counter += 1
           
        
        return "NaN", "NaN", self.seed
    




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "bd Random Range": bd_RandomRange,
    "BD Random Settings": bd_Settings, #legacy
    "bd Variable Settings": bd_Settings,
    "bd Sequencer": bd_Sequencer,
    "bd Variable Settings Draft": bd_SettingsDraft,
    "bd Txt2Img" : bd_txt2img,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "bd_FloatRangeSlider": "bd Random Range",
    "bd_Settings": "BD Random Settings", #legacy
    "bd_Settings": "bd Variable Settings",
    "bd_Sequencer": "bd Sequencer",
    "bd_SettingsDraft": "bd Variable Settings Draft",
    "bd_txt2img": "bd Txt2Img"
}
