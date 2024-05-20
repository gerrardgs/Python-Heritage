import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar, root_scalar

# Define the derivatives function for projectile motion
def derivatives(t, y, params):
    g = 9.81  # acceleration due to gravity (m/s^2)
    x, y_pos, vx, vy = y
    dydt = [vx, vy, 0, -g]
    return dydt

# Define the event function to stop the simulation when the ball reaches the wall
def event_func(t, y, params):
    x, y_pos, vx, vy = y
    wall_distance = params['wall_distance']
    return x - wall_distance

event_func.terminal = True
event_func.direction = 1

# Define the height function to return the height of the baseball when it reaches the wall
def height_func(angle, initial_speed, params):
    angle_rad = np.radians(angle)
    vx = initial_speed * np.cos(angle_rad)
    vy = initial_speed * np.sin(angle_rad)
    initial_conditions = [0, 0, vx, vy]
    
    t_eval = np.linspace(0, 10, 1000)
    result = solve_ivp(derivatives, [0, 10], initial_conditions, args=(params,), events=event_func, t_eval=t_eval)
    
    if result.t_events[0].size > 0:
        y_at_wall = result.y[1, np.argmax(result.t_events[0])]
        print(f"Height at wall for speed {initial_speed} m/s and angle {angle} degrees: {y_at_wall} meters")
        return y_at_wall
    else:
        print(f"Ball did not reach the wall for speed {initial_speed} m/s and angle {angle} degrees")
        return -np.inf  # If the ball doesn't reach the wall, return a very low value

# Define the function to find the optimal angle
def optimal_angle_func(speed, params):
    result = minimize_scalar(lambda angle: -height_func(angle, speed, params), bounds=(0, 90), method='bounded')
    return result.x

# Define the error function for root finding
def error_func(speed, params):
    optimal_angle = optimal_angle_func(speed, params)
    height_at_wall = height_func(optimal_angle, speed, params)
    wall_height = params['wall_height']
    return height_at_wall - wall_height

# Main function to find the minimum speed required to hit a home run
def find_minimum_speed(params):
    # Initial bracket
    lower_bound = 50
    upper_bound = 500
    
    # Check the signs at the initial bounds and adjust if necessary
    while True:
        error_at_lower = error_func(lower_bound, params)
        error_at_upper = error_func(upper_bound, params)
        print(f"Error at speed {lower_bound}: {error_at_lower}")
        print(f"Error at speed {upper_bound}: {error_at_upper}")
        
        if error_at_lower * error_at_upper < 0:
            break
        else:
            # Adjust bounds to find a valid bracket
            if error_at_lower < 0:
                lower_bound /= 2
            else:
                upper_bound *= 2

    # Use root_scalar to find the minimum speed
    result = root_scalar(error_func, args=(params,), bracket=[lower_bound, upper_bound], method='bisect')
    if result.converged:
        min_speed = result.root
        return min_speed
    else:
        raise ValueError("Root finding did not converge")

# Example parameters for Fenway Park
params = {'wall_distance': 310, 'wall_height': 37}

# Find the minimum speed required
min_speed = find_minimum_speed(params)
print(f"Minimum speed to hit a home run: {min_speed} m/s")

# Verify the result
verification_error = error_func(min_speed, params)
print(f"Verification error at speed {min_speed}: {verification_error}")
