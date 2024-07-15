# Sophia Cochis
# Buoyancy calculator


# p1
def calculate_buoyancy(V, density_fluid):
    if (V != int(V) & V != float(V)) | (
        density_fluid != int(density_fluid) & density_fluid != float(density_fluid)
    ):
        return "Error in calculate_buoyancy: non-integer or non-float value detected in V or density_fluid"
    elif V < 0:
        return "Error in calculate_buoyancy: negative V value detected"
    elif density_fluid < 0:
        return "Error in calculate_buoyancy: negative density_fluid value detected."
    else:
        f = V * density_fluid * 9.81
        return f


# p2
def will_it_float(V, mass):
    if (V != int(V) & V != float(V)) | (mass != int(mass) & mass != float(mass)):
        return "Error in will_it_float: non-integer or non-float value detected in V or mass"
    elif V < 0:
        return "Error in will_it_float: negative V value detected"
    elif mass < 0:
        return "Error in will_it_float: negative mass value detected"
    else:
        density = mass / V
        if density > 997:
            return True
        else:
            return False


# p3
def calculate_pressure(depth):
    if depth != int(depth) & depth != float(depth):
        return "Error in calculate_pressure: non-integer or non-float value detected in depth"
    pressure = depth * 9.81 * 1000
    return pressure


# p4
def calculate_acceleration(F, m):
    acceleration = F / m
    return acceleration


# p5
def calculate_angular_acceleration(tau, I):
    angaccel = tau / I
    return angaccel


# p6
def calculate_torque(F_magnitude, F_direction, r):
    I = F_magnitude * r**2
    trq = I * F_direction
    return trq


# p7
def calculate_moment_of_inertia(m, r):
    I = m * r**2
    return I


# p8
def calculate_AUV_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if F_magnitude > 100 or F_magnitude < 0:
        return "Error in calculate_AUV_acceleration: thruster force value out of range"
    elif F_angle > 30 or F_angle < -30:
        return "Error in calculate_AUV_acceleration: thruster angle value out of range"
    else:
        acceleration = F_magnitude / mass
    return acceleration


acceleration = calculate_AUV_acceleration(1, 2, 3, 4, 5)


def calculate_AUV_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if F_magnitude > 100 or F_magnitude < 0:
        return "Error in calculate_AUV_angular_acceleration: thruster force value out of range"
    elif F_angle > 30 or F_angle < -30:
        return "Error in calculate_AUV_angular_acceleration: thruster angle value out of range"
    else:
        angular_acceleration = F_magnitude / mass
    return angular_acceleration


angular_acceleration = calculate_AUV_angular_acceleration(1, 2, 3, 4)


# p9
def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    pass


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    pass
