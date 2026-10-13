import taichi as ti
from utils import get_color

@ti.kernel
def render_mandelbrot(pixels: ti.template(), res_x: int, res_y: int, zoom: float, offset_x: float, offset_y: float, max_iter: int, pal_idx: int):
    for i, j in pixels:  
        cx = (i - res_x / 2) / (res_y / 2) * zoom + offset_x
        cy = (j - res_y / 2) / (res_y / 2) * zoom + offset_y
        
        x = 0.0
        y = 0.0
        
        iterations = 0
        
        while x**2 + y**2 < 4.0 and iterations < max_iter:
            xtemp = x**2 - y**2 + cx
            y = 2 * x * y + cy
            x = xtemp
            iterations += 1
            
        if iterations == max_iter:
            pixels[i, j] = ti.cast(ti.math.vec3(0.0, 0.0, 0.0), ti.f32)
        else:
            dist_sq = ti.cast(x**2 + y**2, ti.f32)
            log_z = ti.math.log(dist_sq) / 2.0
            
            log_2 = 0.69314718
            nu = ti.math.log(log_z / log_2) / log_2
            
            smooth_i = ti.cast(iterations, ti.f32) + 1.0 - nu
            t = smooth_i / 50.0 
            
            pixels[i, j] = ti.cast(get_color(t, pal_idx), ti.f32)