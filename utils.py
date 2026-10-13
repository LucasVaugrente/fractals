import taichi as ti

@ti.func
def get_color(t: float, palette_idx: int):
    a = ti.math.vec3(0.0, 0.0, 0.0)
    b = ti.math.vec3(0.0, 0.0, 0.0)
    c = ti.math.vec3(0.0, 0.0, 0.0)
    d = ti.math.vec3(0.0, 0.0, 0.0)

    if palette_idx == 0:
        a = ti.math.vec3(0.5, 0.5, 0.5)
        b = ti.math.vec3(0.5, 0.5, 0.5)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.0, 0.33, 0.67)


    elif palette_idx == 1: # Dark Blue
        a = ti.math.vec3(0.0, 0.0, 0.5)
        b = ti.math.vec3(0.0, 0.0, 0.5)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.0, 0.0, 0.75)

    elif palette_idx == 2: # Dark Green
        a = ti.math.vec3(0.0, 0.5, 0.0)
        b = ti.math.vec3(0.0, 0.5, 0.0)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.0, 0.75, 0.0)

    elif palette_idx == 3: # Dark Red
        a = ti.math.vec3(0.5, 0.0, 0.0)
        b = ti.math.vec3(0.5, 0.0, 0.0)
        c = ti.math.vec3(1.0, 1.0, 1.0)
        d = ti.math.vec3(0.6, 0.0, 0.0)

    return a + b * ti.math.cos(6.28318 * (c * t + d))