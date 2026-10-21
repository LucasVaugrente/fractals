import taichi as ti

@ti.func
def get_color(t: float, palette_idx: int):
    a = ti.math.vec3(0.0, 0.0, 0.0)
    b = ti.math.vec3(0.0, 0.0, 0.0)
    c = ti.math.vec3(0.0, 0.0, 0.0)
    d = ti.math.vec3(0.0, 0.0, 0.0)

    if palette_idx == 0: # Dark Blue
        a = ti.math.vec3(0.0, 0.0, 0.5)
        b = ti.math.vec3(0.0, 0.0, 0.5)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.0, 0.0, 0.75)

    elif palette_idx == 1: # Dark Green
        a = ti.math.vec3(0.0, 0.5, 0.0)
        b = ti.math.vec3(0.0, 0.5, 0.0)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.0, 0.75, 0.0)

    elif palette_idx == 2: # Dark Red
        a = ti.math.vec3(0.5, 0.0, 0.0)
        b = ti.math.vec3(0.5, 0.0, 0.0)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.6, 0.0, 0.0)

    elif palette_idx == 3:
        a = ti.math.vec3(0.34, 0.22, 1.00)
        b = ti.math.vec3(0.00, 0.77, 0.45)
        c = ti.math.vec3(2.07, 0.80, 1.00)
        d = ti.math.vec3(0.00, 0.35, 0.46)

    elif palette_idx == 4:
        a = ti.math.vec3(0.80, 0.24, 0.00)
        b = ti.math.vec3(0.19, 0.54, 0.00)
        c = ti.math.vec3(1.76, 1.62, 1.00)
        d = ti.math.vec3(0.36, 0.35, 0.23)

    return a + b * ti.math.cos(6.28318 * (c * t + d))