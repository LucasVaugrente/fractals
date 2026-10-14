import taichi as ti
from utils import get_color

@ti.kernel
def render_mandelbrot(
    pixels: ti.template(), 
    buf_x: int, 
    buf_y: int, 
    aspect_ratio: ti.f64, 
    zoom: ti.f64, 
    offset_x: ti.f64, 
    offset_y: ti.f64, 
    max_iter: int, 
    pal_idx: int
):
    for i, j in pixels:  
        u = (ti.cast(i, ti.f64) / buf_x - 0.5) * 2.0 * aspect_ratio
        v = (ti.cast(j, ti.f64) / buf_y - 0.5) * 2.0
        
        cx = u * zoom + offset_x
        cy = v * zoom + offset_y
        
        x = ti.cast(0.0, ti.f64)
        y = ti.cast(0.0, ti.f64)
        iterations = 0
        
        while x**2 + y**2 < 4.0 and iterations < max_iter:
            xtemp = x**2 - y**2 + cx
            y = 2.0 * x * y + cy
            x = xtemp
            iterations += 1
            
        if iterations == max_iter:
            pixels[i, j] = ti.math.vec3(0.0, 0.0, 0.0)
        else:
            dist_sq = ti.cast(x**2 + y**2, ti.f32)
            log_z = ti.math.log(dist_sq) / 2.0
            
            log_2 = 0.69314718
            nu = ti.math.log(log_z / log_2) / log_2
            
            smooth_i = ti.cast(iterations, ti.f32) + 1.0 - nu
            t = smooth_i / 50.0 
            
            pixels[i, j] = get_color(t, pal_idx)