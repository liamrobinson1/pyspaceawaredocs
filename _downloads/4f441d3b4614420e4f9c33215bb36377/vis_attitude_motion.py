"""
Rigid Body Torque Free Attitudes
================================

Animates the attitude motion of an object in torque free motion
"""

import pyspaceaware as ps
import numpy as np
import pyvista as pv

(dates, epsecs) = ps.date_linspace(
    ps.now(), ps.now() + ps.seconds(10), 300
)
obj = ps.SpaceObject("tess.obj", satnum=36411)
obj_attitude = ps.RbtfAttitude(
    w0=1 * np.array([1, 1, 1]),
    q0=ps.hat(np.array([0, 0, 0, 1])),
    itensor=obj.principal_itensor,
)

(q, w) = obj_attitude.propagate(epsecs)

ps.vis_attitude_motion(
    obj, q, "tess.gif", framerate=30, background_color="black"
)
