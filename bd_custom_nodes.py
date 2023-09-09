import math
import random
import re

   

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
    CATEGORY = "BD Nodes"

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
                "randomize": (["enable", "disable"],),
                "variation_amount": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "refiner_amount": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01, "display": "number"}),
                # "output": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "0"
                # }),
            },
        }

    RETURN_TYPES = ("FLOAT", "INT", "FLOAT", "INT")
    RETURN_NAMES = ("cfg", "steps", "denoise", "refiner start")
    FUNCTION = "randomize_it"
    OUTPUT_NODE = True
    CATEGORY = "BD Nodes"

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
    def randomize_it(cfg, steps, variation_amount, denoise, seed, randomize, refiner_amount):

        #exit early  and just return the settings
        if randomize == "disable":
            refiner_start = bd_Settings.calc_refiner(steps, refiner_amount)
            return (cfg, steps, denoise, refiner_start)
        
        
        #set our new seed
        random.seed(seed)

        outcfg = bd_Settings.randomize(cfg, variation_amount)
        outsteps = math.floor(bd_Settings.randomize(float(steps), variation_amount))
        outdenoise = bd_Settings.randomize(denoise, variation_amount)
        outdenoise = bd_Settings.clamp(outdenoise, 0.0, 1.0)        
        refiner_start = bd_Settings.calc_refiner(outsteps, refiner_amount)


        print(f"bd random cfg is {outcfg} and random step amount is {outsteps}, denoise amt is {outdenoise}, refiner start is {refiner_start}")

        #output = str(outFloat)

        return outcfg, outsteps, outdenoise, refiner_start
    


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
    CATEGORY = "BD Nodes"

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
    "BD Random Range": bd_RandomRange,
    "BD Random Settings": bd_Settings, #legacy
    "BD Settings": bd_Settings,
    "BD Sequencer": bd_Sequencer
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "bd_FloatRangeSlider": "BD Random Range",
    "bd_RandomizeSettings": "BD Random Settings", #legacy
    "bd_RandomizeSettings": "BD Settings",
    "bd_Sequencer": "BD Sequencer"
}
