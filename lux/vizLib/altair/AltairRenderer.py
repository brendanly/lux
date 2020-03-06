import lux
from lux.vizLib.altair.BarChart import BarChart
from lux.vizLib.altair.ScatterChart import ScatterChart
from lux.vizLib.altair.LineChart import LineChart
from lux.vizLib.altair.Histogram import Histogram

class AltairRenderer:
	"""
	Renderer for Altair Charts
	"""
	def __init__(self):
		pass
	def __repr__(self):
		return f"AltairRenderer"
	def createVis(self,view):
		"""
		Input DataObject and return a visualization specification
		
		Parameters
		----------
		view: lux.view.View
			Input View (with data)
		
		Returns
		-------
		chart : altair.Chart
			Output Altair Chart Object
		"""		
		if (view.mark =="histogram"):
			chart = Histogram(view)
		elif (view.mark =="bar"):
			chart = BarChart(view)
		elif (view.mark =="scatter"):
			chart = ScatterChart(view)
		elif (view.mark =="line"):
			chart = LineChart(view)
		chart = chart.chart.to_dict()
		chart["data"] =  { "values": view.data.to_dict(orient='records') }
		chart["width"] = 160
		chart["height"] = 150
		return chart