from .backend import SimulationBackend

import os
import importlib
import sys

sys.path.append("C:\\Users\\Jason\\Downloads\\CellModeller5\\CellModeller\\build\\lib.win-amd64-3.8")

import CellModeller5 as cm5

class CellModeller5Backend(SimulationBackend):
	def __init__(self, params):
		super().__init__(params)

		self.params = params
		self.simulator = None
	
	def initialize(self):
		self.simulator = cm5.Simulator()
	
	def step(self):
		self.simulator.step()

	def write_step_files(self):
		base_file_name = "step-%05i" % self.simulator.get_step_index()

		step_path = os.path.join(self.params.sim_root_dir, f"{base_file_name}.cm5_step")
		viz_bin_path = os.path.join(self.params.cache_dir, f"{base_file_name}.cm5_viz")

		step_file_relative = os.path.join(".", f"{base_file_name}.cm5_step")
		cached_file_relative = os.path.join(self.params.cache_relative_prefix, f"{base_file_name}.cm5_viz")

		# Write step file
		self.simulator.dump_to_step_file(str(step_path))

		# Write viz file
		self.simulator.dump_to_viz_file(str(viz_bin_path))

		return step_file_relative, cached_file_relative

	def shutdown(self):
		del self.simulator
		self.simulator = None