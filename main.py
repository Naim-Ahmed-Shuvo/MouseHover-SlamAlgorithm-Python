from slam import env, sensors
import pygame


environment = env.build_environment((600, 1200))
environment.original_map = environment.map.copy()

laser = sensors.laser_sensor(200, environment.original_map, uncertainity=(0.5, 0.01))

# filling black color
environment.map.fill((0, 0, 0))
environment.info_map = environment.map.copy()

running = True

while running:
    sensor_on = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_focused():
            sensor_on = True

        elif not pygame.mouse.get_focused():
            sensor_on = False

    if sensor_on:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sens_obstacles()
        environment.data_storage(sensor_data)
        environment.show_sensors_data()

    environment.map.blit(environment.info_map, (0, 0))
    pygame.display.update()
