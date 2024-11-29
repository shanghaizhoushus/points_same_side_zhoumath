# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:34:41 2024

@author: zhoumath
"""

#Import packages
import numpy as np

def _points_is_one_side(points):
    """
    Simulate whether a set of random points in a unit circle are concentrated on the same side (semi-circle).
    :param points: The number of random points to generate.
    :return: True if the points are concentrated on the same side (semi-circle), False otherwise.
    """
    arcs = np.zeros(points)
    i = 0
    while True:
        a = np.random.rand(2) * 2 - 1
        if np.linalg.norm(a) < 1:
            if a[0] > 0 and a[1] > 0:
                arc = np.arctan(a[1]/ a[0])
            elif a[0] < 0 and a[1] > 0:
                arc = np.pi - np.arctan(np.abs(a[1]/ a[0]))
            elif a[0] < 0 and a[1] < 0:
                arc = np.pi + np.arctan(np.abs(a[1]/ a[0]))
            elif a[0] > 0 and a[1] < 0:
                arc = 2*np.pi - np.arctan(np.abs(a[1]/ a[0]))
            arcs[i] = arc
            i += 1
        if i == points:
            break
    arcs = np.sort(np.array(arcs))
    max_gap = np.max(np.array([np.max(np.diff(arcs)), 2*np.pi + arcs[0] - arcs[-1]]))
    return max_gap > np.pi

def monto_carlo_points(num_iter, points):
    """
    Perform a Monte Carlo simulation to estimate the probability of points being concentrated 
    on the same side of a circle.
    
    :param num_iter: The number of Monte Carlo simulations to run.
    :param points: The number of points to generate in each simulation.
    :return: None, but prints the average probability of points being concentrated on one side.
    """
    records = np.zeros(num_iter)
    for i in range(num_iter):
        records[i] = _points_is_one_side(points)
    print(records.mean())

monto_carlo_points(100000, 4)







