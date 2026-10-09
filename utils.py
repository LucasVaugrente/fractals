import taichi as ti

@ti.func
def get_color(t: float, palette_idx: int):
    a = ti.math.vec3(0.5, 0.5, 0.5)
    b = ti.math.vec3(0.5, 0.5, 0.5)
    c = ti.math.vec3(1.0, 1.0, 1.0)
    d = ti.math.vec3(0.0, 0.0, 0.0)
    
    if palette_idx == 0:
        # Bleu electrique / Or
        d = ti.math.vec3(0.0, 0.33, 0.67)
    elif palette_idx == 1:
        # Arc-en-ciel
        d = ti.math.vec3(0.0, 0.1, 0.2)
    elif palette_idx == 2:
        # Rose / Violet 
        d = ti.math.vec3(0.3, 0.2, 0.2)
    elif palette_idx == 3:
        # Ambiance Feu / Magma
        c = ti.math.vec3(1.0, 1.0, 0.5)        
        d = ti.math.vec3(0.8, 0.9, 0.3)
        
    return a + b * ti.math.cos(6.28318 * (c * t + d))