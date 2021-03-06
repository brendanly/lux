<p align="center"><a href="#"><img width=77% alt="" src="https://github.com/lux-org/lux/blob/master/examples/img/logo.png?raw=true"></a></p>
<h2 align="center">A Python API for Intelligent Visual Discovery</h2>

<p align="center">
    <a href="https://travis-ci.org/lux-org/lux">
        <img alt="Build Status" src="https://travis-ci.org/lux-org/lux.svg?branch=master" align="center">
    </a>
    <a href="https://badge.fury.io/py/lux-api">
        <img src="https://badge.fury.io/py/lux-api.svg" alt="PyPI version" height="18" align="center">
    </a>
    <a href='https://lux-api.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/lux-api/badge/?version=latest' alt='Documentation Status'  align="center"/>
    </a>
</p>

Lux is a Python library that makes data science easier by automating certain aspects of the data exploration process. Lux is designed to facilitate faster experimentation with data, even when the user does not have a clear idea of what they are looking for. Lux is integrated with [an interactive Jupyter widget](https://github.com/lux-org/lux-widget) that allows users to quickly browse through large collections of data directly within their Jupyter notebooks.

Here are some [slides](http://dorisjunglinlee.com/files/RISE_Winter_Retreat_Slides.pdf) from a recent talk on Lux.

## Quick Start

Install the Python Lux API through [PyPI](https://pypi.org/project/lux-api/): 

```bash
pip install lux-api
```

Install the Lux Jupyter widget through [npm](https://www.npmjs.com/package/lux-widget): 

```bash
npm i lux-widget
```

## Features
<p align="center">
    <img src="https://github.com/lux-org/lux/blob/master/examples/img/capabilities.png?raw=true"
        alt="Lux capabilities"
        width="400px"
        height="200px" />
</p>
Lux provides a suite of capabilities as outlined in the hierarchy above from the most basic (automatic encoding) to the most complex (predictive recommendations).

### Automatic Encoding: 
Lux is built on the principle that users should always be able to visualize anything they specify, without having to think about *how* the visualization should look like. Lux automatically determines the mark and channel mappings based on a set of [best practices](http://hosteddocs.ittoolbox.com/fourshowmeautomaticpresentations.pdf) from [Tableau](https://www.tableau.com). The visualizations are rendered via [Altair](https://github.com/altair-viz/altair/tree/master/altair) into [Vega-Lite](https://github.com/vega/vega-lite) specifications.

```python    
    import lux
    # Load a dataset into Lux
    dataset = lux.Dataset("data/car.csv")

    dobj = lux.DataObj(dataset,[lux.Column("Acceleration"),
                                lux.Column("Horsepower")])
```    
<img src="https://github.com/lux-org/lux/blob/master/examples/img/specifiedVis.png?raw=true"
     alt="Specified Visualization"
     style="width:200px" />

### Search Space Enumeration: 

Lux implements a set of enumeration logic that generates a visualization collection based on a partially specified query. Users can provide a list or a wildcard to iterate over combinations of filter or attribute values and quickly browse through large numbers of visualizations. The partial specification is inspired by existing work on query languages for visualization languages, including [ZQL](https://github.com/vega/compassql) and [CompassQL](https://github.com/vega/compassql).

Here, we want to look at how the attributes `Weight` and `Displacement` depend on all other dimension variables.

```python
dobj = lux.DataObj(dataset,[lux.Column(["Weight","Displacement"]),lux.Column("?",dataModel="dimension")])
```

<img src="https://github.com/lux-org/lux/blob/master/examples/img/PartialSpecificationDemo.gif?raw=true"
     alt="Specified Visualization"
     style="width:600px" />

### Analytics Modules: 

Lux comes with a set of analytics capabilities. We can compose multiple DataObjects or DataObjectCollections to perform a specified task. 

For example, we can ask which car brands have a time series of Displacement similar to that of Pontiac cars. 
```python
    query = lux.DataObj(dataset,[lux.Column("Year",channel="x"),
                            lux.Column("Displacement",channel="y"),
                            lux.Row("Brand","pontiac")])

    dobj = lux.DataObj(dataset,[lux.Column("Year",channel="x"),
                                lux.Column("Displacement",channel="y"),
                                lux.Row("Brand","?")])

    result = dobj.similarPattern(query,topK=5)
```
<img src="https://github.com/lux-org/lux/blob/master/examples/img/SimilarityDemo.gif?raw=true"
     alt="Similar Patterns"
     style="width:600px" />

### Predictive Recommendation: 

Lux has an extensible logic that determines the appropriate analytics modules to call based on the user’s current state (i.e., the attributes and values they’re interested in). By calling the `showMore` command, Lux guides users to potential next-steps in their exploration.

In this example, the user is interested in `Acceleration` and `Horsepower`, Lux generates three sets of recommendations, organized as separate tabs on the widget.
 
```python
    dobj = lux.DataObj(dataset,[lux.Column("Acceleration",dataModel="measure"),
                                lux.Column("Horsepower",dataModel="measure")])
    result = dobj.showMore()
```
<img src="https://github.com/lux-org/lux/blob/master/examples/img/ShowMore.gif?raw=true"
     alt="Show More Recommendations"
     style="width:600px" />
 
 The left-hand side of the widget shows the Current View, which corresponds to the attributes that have been selected. On the right, Lux recommends:

 - Enhance: Adds an additional attribute to the current selection
 - Filter: Adds a filter to the current selection, while keeping X and Y fixed
 - Generalize: Removes an attribute to display a more general trend

## Manual Installation (dev)

There are two components of Lux: 1) Python Lux API (this repo)and 2) the Jupyter widget frontend (inside [lux-widget](https://github.com/lux-org/lux-widget)). 

To install the Python Lux API: 
```bash
pip install --user -r requirements.txt
cd lux/
python setup.py install
```
To install the widget, we need to install webpack:  
```bash
npm install --save-dev webpack webpack-cli
```
Then, we can install the [Lux Jupyter widget](https://github.com/lux-org/lux-widget) using the custom installation script: 
```bash
git clone git@github.com:lux-org/lux-widget.git
cd lux-widget/
npm install
bash install.sh
```

For more detailed examples of how to use Lux, check out this demo [notebook](https://github.com/lux-org/lux/blob/master/examples/demo.ipynb). 

Lux is undergoing active development. Please report any bugs, issues, or requests through [Github Issues](https://github.com/lux-org/lux/issues).
