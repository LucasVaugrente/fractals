import taichi as ti
from tools import Camera
from fractals.julia import render_julia
from fractals.mandelbrot import render_mandelbrot

ti.init(arch=ti.gpu, default_fp=ti.f32)

res_x, res_y = 1200, 800
pixels = ti.Vector.field(n=3, dtype=ti.f32, shape=(res_x, res_y))

c_real, c_imag = -0.835, 0.0 
max_iterations = 25000

window = ti.ui.Window("Fractals", (res_x, res_y))
canvas = window.get_canvas()
cam = Camera(res_x, res_y)

cam.offset_x = -0.5

while window.running:
    cam.handle_input(window)
    
    # render_julia(pixels, res_x, res_y, c_real, c_imag, cam.zoom, cam.offset_x, cam.offset_y, max_iterations, cam.palette)
    render_mandelbrot(pixels, res_x, res_y, cam.zoom, cam.offset_x, cam.offset_y, max_iterations, cam.palette)
    
    canvas.set_image(pixels)
    window.show()