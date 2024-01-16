"""
Created on Sun Apr 30 13:59:30 2023

@author: Piotr Rędziński

python script for keywords based classification
"""
from collections import defaultdict, Counter
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
import pandas as pd

      

df = pd.read_excel('C:/ProjektyPython/textClasification/input/ALL PAPERS MAY10.xlsx')

filtered = df[df['Abstract'].notna()]
#filtered = filtered.fillna(0)





tools=["algorithm proposed",
"new device",
"task head",
"network",
"game",
"digital online tool",
"interaction process",
"analytics system",
"new digital products",
"services",
"practical technical tools",
"scalable toolbox",
"new end-to-end dual-stream architecture",
"device was prototyped",
"wearable system",
"prototype"
"development of the IoT system layered architecture",
"interactive online map",
"intuitive and simplified 3D modeling platform",
"module",
"innovative platform",
"novel national spatial data infrastructure",
"original tool was extended",
"agent-based model",
"intuitive navigation interface",
"Siamese network",
"planning application",
"interface between",
"platform",
"novel version",
"encoder and decoder"
]

review_applications = ["comparison"]

#ReviewApplications
applied=["adopted",
"employed"]
applied_method=["method"]

others=["tool","tools"]


planning=["urban design",
"landscape design",
"environmental design",
"spatial planning",
"landscape planning",
"urban planning",
"environmental planning"]

exclusions=["transport",
"energy",
"building design",
"service planning",
"education",
"management",
"statistics",
"literature review"
]


''' techology '''
cad=["cad","computer-aided","computer aided","autocad"]

data_science=["data science"]
data_minig=["data mining","inteligent mining"]
big_data=["big data"]
crowdsourcing=["crowdsourcing","social sensing","city sensing",
"citizen-science","citizen science","user-generated content",
"user-driven cartography","msp challenge","crowd","PPGIS","PGIS","crowdsourced",
"participatory mapping","participatory map",
"citizen-led spatial information system"]


open_data=["open data",
"publicly available data",
"copernicus",
"open street map",
"inspire",  #----------
"google street view",
"check all algorithms",
"noaa's satellite and information services",
"nesdis",
"openstreetmap",
"open data sources",
"openly shared resources",
"webgis",
"isprs dataset",
"urban atlas",
"lightgbm",
"msp challenge", #duplikat z crowdsourcing
"spot 6",
"open-source gis",
"nsdi"
]

#"OthersData"
others_data=['coklimax',
 'spatial data infrastructure blockchain',
 'data-driven approach, smart city',
 'data flow',
 'wildlife tracking data',
 'data platform',
 'the data-driven evidential belief function model',
 'benchmark dataset',
 "tourists' online reviews",
 'open data, geospatial big data',
 'google earth',
 'street view',
 'the spatial data infrastructures',
 'social sensing data',
 'openstreetmap, social sensing data',
 'multi density data',
 'geospatial big-data',
 'automated data collection',
 '(ahp)-based data mining',
 'open geodata integration',
 'smart sensing technology',
 'urban atlas',
 'geospatial data',
 'interactive data',
 'geospatial data; street view imges',
 'geo-database',
 'street view image',
 'openstreetmap implemented as project ohana (open-source heatmap and analytics for nationwide amenities accessibility in the philippines)',
 'landsupport',
 'openstreetmap',
 'open data',
 'hybrid data',
 'open street maps',
 'integrates multisource geographic data',
 'spot 6',
 'indicatores colected, google street view',
 'inspire- land use map',
 'information visualization',
 'webgis',
 'crowdsourcing',
 'street view images',
 'open data platforms',
 'assimilating web-based datasets',
 'msp challenge']


others_data_open_data=['coklimax',
 'open data, geospatial big data',
 'google earth',
 'street view',
 'openstreetmap, social sensing data',
 'open geodata integration',
 'urban atlas',
 'geospatial data',
 'street view image',
 'geospatial data; street view imges',
 'openstreetmap implemented as project ohana (open-source heatmap and analytics for nationwide amenities accessibility in the philippines)',
 'landsupport',
 'openstreetmap',
 'open data',
 'open street maps',
 'spot 6',
 'indicatores colected, google street view',
 'inspire- land use map',
 'webgis',
 'street view images',
 'assimilating web-based datasets',
 'msp challenge']

others_data_crowdsourcing=['openstreetmap',
 "tourists' online reviews",
 'open data, geospatial big data',
 'openstreetmap, social sensing data',
 'social sensing data',
 'geospatial data',
 'inspire- land use map',
 'crowdsourcing',
 'msp challenge']

others_data_big_data=['geospatial big-data',
 'openstreetmap',
 'open geodata integration',
 'open data, geospatial big data',
 'data-driven approach, smart city',
 'openstreetmap, social sensing data',
 'geospatial data',
 'inspire- land use map']

others_data_data_minig=['(ahp)-based data mining']

others_data_data_science=[]
excl_other_data=['coklimax',
 'open data, geospatial big data',
 'google earth',
 'street view',
 'openstreetmap, social sensing data',
 'open geodata integration',
 'urban atlas',
 'geospatial data',
 'street view image',
 'geospatial data; street view imges',
 'openstreetmap implemented as project ohana (open-source heatmap and analytics for nationwide amenities accessibility in the philippines)',
 'landsupport',
 'openstreetmap',
 'open data',
 'open street maps',
 'spot 6',
 'indicatores colected, google street view',
 'inspire- land use map',
 'webgis',
 'street view images',
 'assimilating web-based datasets',
 'msp challenge',
 'openstreetmap',
 "tourists' online reviews",
 'open data, geospatial big data',
 'openstreetmap, social sensing data',
 'social sensing data',
 'geospatial data',
 'inspire- land use map',
 'crowdsourcing',
 'msp challenge',
 'geospatial big-data',
 'openstreetmap',
 'open geodata integration',
 'open data, geospatial big data',
 'data-driven approach, smart city',
 'openstreetmap, social sensing data',
 'geospatial data',
 'inspire- land use map',
 '(ahp)-based data mining']

other_other_data = ['tool', 'tools']


#other_data=open_data
vr=["vr","ar","mr","immersive virtual technologies",
    "xr","ivr","extended reality","virtual reality",
    "augmented reality","diminished reality","mixed reality","virtual environments","cave2","cave"]

ai_related=["segmentation",
"extraction",
"convolutional neural networks",
"cnn","rnn","dnn",
"neural model",
"neural network",
"genetic algorithm"
"fuzzy k",
"k-mean",
"asymmetric convolution block",
"natural language processing",
"automatic recognition",
#"ai"
]

deep_learning=["deep learning","cnn","DeepLabV3+","neural",
               "u-net","generalized adversarial networks",
               "gans","encoder and decoder","flus"]
artificial_inteligence=["artificial intelligence","ai"]
machine_learning=["machine learning","supervised learning","supervised classification",
                  "unsupervised classification",
                  "generalized adversarial networks","random forest","xgboost",
                  "support vector machine","clustering","decision tree",
                  "object based image analysis","obia","sentiment analysis"]
mas=["mas","multi-agents model","agent-based","agent","olympus","agents"]


#"OthersAI",
others_ai=['supervised classification',
 'genetic algorithm',
 'federated learning (fl)',
 'non-dominated sorting genetic algorithm-ii-optimization',
 'location semantic, svi-derived straightforward algorithm',
 'semantic segmentation',
 'supervised learning',
 'fuzzy k-means clustering algorithm',
 'the single channel algorithm (sca)',
 'computer vision (cv) technology',
 'computer image processing, image entropy calculation, and colour mapping to process the data',
 "agent-based model named 'd-fmcities'",
 'optimization:  multi-task neural network is developed; multi-label classification process',
 'natural language processing',
 'computer vision techniques',
 'segmentation',
 'ann models, data scenarios in 5-year forecast',
 'convolutional neural networks, segmentation',
 'geoai',
 'pso-bp neural network model']


#"Remote sensing",
remote_sensing = ['remote sensing',"rs"] #,"satelite images"]
lidar=["lidar"]
#ranging=["ranging instruments"]
#hyperspectral=["hyperspectral instruments"]
#scatterometers=["scatterometers"]
#imaging_radar=["imaging radar"]
#spowertpower=["spowertpower"] 
#polarimetric=["polarimetric"]
#sounding=["sounding"]
#"OthersRS",
others_rs=['moderate-resolution imaging spectroradiometer (modis)',
 'satellite-based data products',
 'photo-identification',
 'photogrammetry',
 'data',
 'remote sensing image fusion techniques']


#"Social Media",
socialmedia=["socialmedia","social media"]
social_networks=["socialnetworks","social networks","social network","facebook","flickr","instagram","twitter"]
social_news=["socialnews","social news"]
blogging=["blogging","blog"]
bookmarking=["bookmarking","book marking"]
media_sharing=["mediasharing","media sharing","flickr"] #flickr?
socialmedia=["socialmedia","social media"]
#"OthersSocialMedia",
others_socialmedia=['fb',
 'geotaging, geo-referenced photo',
 'flickr; geotagged photos',
 'geocomputational scenario, like crowdsourcing, crowdcasting, web 2.0, geotagging, geo-wiki, geoblog, georss feeds, and geocitizen']
    
#"DigitalModelling",
bim=["bim","bps","bim-gis","parametric"]
sim=["sim","system information model","system information modelling"]
lim=["lim","landscape information model","landscape information modelling"
     ,"land information modelling","land information model"]
pointcloud=["terestial","point cloud","point-cloud"] #+3d scanning
rendering=["rendering"]
n3dscaning=["3dscanning","lidar","airborne laser scanning","als","terrestrial laser scanning"] #lidar?
statistical_modeling=["statistical modelling",
"cellular automata",
"cellular-automata",
"marcov",
"markov",
"forest-marcov",
"forest-markov",
"regression tree",
"regression",
"regression model",
"tree-regression",
"multivariate regression",
"logistic regression",
"logistic-regression",
"lotka-volterra",
"lotka volterra",
"kalman filter",
"hierarchical bayesian modeling",
"bayesian",
"random forest",
"nonlinear programming",
"gradient projection method",
"interaction fixed effect",
"marine predator algorithm",
"mapreduce",
"flood frequency analyses",
"tfm-ext",
"structural equation",
"gradient analysis",
"moving window",
"time series",
"correlation coefficient",
"spatiotemporal modeling",
"statistically",
"density distribution",
"clustering",
"spatial optimization",
"structural equation modeling",
"monte carlo simulation",
"fluid dynamics", 
"mesonh-surfex-teb mesoscale atmospheric model",
"3d steady-state reynolds-averaged navier-stokes simulations",
"system dynamics",
"causal inference",
"geostatistics",
"geodetector",
"nas algorithm",
"mathematical:python",
"parallelized large eddy simulation (les) model palm",
"invest urban cooling model",
"invest model",
"template matching",
"geometric modelling by parametric modelling tools",
"simulation of environmental parameters by using bps tools",
"shape optimization by using an evolutionary algorithm",
"numerical simulations",
"urans",
"unsteady reynolds-averaged navier-stokes",
"equations and the kappa-omega sst model",
"htb2 and the virvil plugin",
"k-means and agglomerative hierarchical clustering",
"pollutant dispersion",
"predicting esp-flus model",
"conefor model",
"longitudinal",
"distribution model",
"circuit models",
"multiple least cost corridors",
"mlcc",
"carrying capacity",
"gaussian",
"spatial syntax",
"space syntax",
"logit modeling",
"stochastic",
"activity-based models",
"graph theory",
"minimum spanning tree",
"euclidean steiner tree",
"steiner points",
"kernel density",
"entropy weighing method",
"virtual simulation",
"fire modeling",
"modeling urban street lighting",
"gravitation model",
"mathematical model",
"mathematical modelling",
"modelling of carbon emission",
"land use–transport interaction",
"luti",
"shannon's entropy",
"social force model",
"simulation of crowds",
"crowd simulation",
"regional economic input-output model",
"reim",
"land use evolution and impact assessment model",
"leam",
"statistical data processing",
"estimation model",
"emission model",
"generative model",
"mechanistic model", 
"computational geometry",
"sweep line paradigm",
"fréchet distance",
"frechet distance",
"data fusion",
"loop-detector data model",
"generalized additive model", 
"generalized additive modeling", 
"gam",
"eutrophication model",
"water quality models",
"land-use changes model",
"land-use changes modeling",
"fuzzy mathematics",
"universal soil loss equation",
"usle", 
"erosion model",
"soil land inference model",
"solim",
"fuzzy logic",
"least-cost-path analysis",
"path-analysis"
]


n3dModelling=["3dmodelling",
              "3d modelling",
              "3d model",
              "digital surface model",
              "digital twins",
              "digital terrain model",
              "dst",
              "dtm",
              "digital elevation model",
              "dem",
              "3d computational",
              "3d computer",
              "3d steady-state reynolds-averaged",
              "3d representations",
              "3d scenes",
              "3d visualisation",
              "3d tessellated",
              "three-dimensional modeling",
              "three-dimensional modelling",
              "three-dimensional display",
              "city geography markup language",
              "citygml",
              "geo-referenced model",
              "3d geographical information system",
              "3d city modelling",
              "3d city model",
              "sleuth",
              "three dimensional computer graphic",
              "3d data",
              "rhino3d",
              "rhinoceros",
              "grashopper3d",
              "3d microclimatic model",
              "3d topographic data",
              "limulator",
              "photogrammetry"
              ]

#fluid dynamics

mcda=["ahp","analytical hierarchy process","mcda","multiobjective",
"multicriteria decision",
"multi criteria evaluation",
"multicriteria evaluation",
"multi-criteria analysis",
"multi criteria analysis", 
"multi-objective approach",
"multi-objective land allocation","mola",
"pca",
"fuzzy-set",
"heuristic algorithm",
"multivariant analysis",
"topsis",
"super decision",
"gaussian process classification",
"weight-based generalized objective",
"godl",
"god model",
"wlc",
"anp",
"mcdm",
"gis-mcda",
"mce-gis"
]

pss_dss=["pss/dss",
         "planning support system",
         "decision support system",
         "decision-support system",
         "pss",
         "dss",
         "toolbox for urban planning",
         "conefor",
         "decision support tools"
         ]

hydrological=["hydrological model",
              "hydrologicalmodel",
              "swmm",
              "flood",
              "watershed",
              "groundwater",
              "storm water",
              "stormwater",
              'hydrodynamic model',
              "flooding"
              ]



climatic = ['air pollution',
            'airpollution',
            'heat island',
            'heat-island',
            'envi-met',
            "heat island","lands surface temperature",
            'land surface temperature',
            "thermal comfort",
            "air flow",
            "urban heat island",
            "uhi","wind",
            "ground surface temperature",
            "street canyon",
            "sky view factor",
            "predict air quality",
            "pm2.5 concentration prediction",
            "air quality modeling",
            "spatial rainfall distribution",
            "modelling of carbon emission",
            "carbon emission model",
            "noise propagation",
            "thermal environment",
            "local climate zone",
            "emission estimation",
            "pollutant dispersion"
]

conectivity = ['biodiversity models',
               'ecological corridors',
               'ecological security pattern',
               "ecological connectivity",
               "spatial connectivity",
               "maxent model",
               "species distribution model",
               "spatial ecological networks", 
               "landscape permeability",
               "landscape connectivity",
               "biophysical modeling"
               ]


statistical_modeling=statistical_modeling+hydrological+climatic+conectivity+mcda
statistical_modeling=list(set(ai_related+deep_learning+artificial_inteligence+machine_learning+mas+others_ai+statistical_modeling))

other_modelling=["digital modelling",
                 "pollution",
                 "heat island",
                 "lands surface temperature",
                 "lst",
                 "air flow",
                 "uhi",
                 "wind",
                 "biodiversity models",
                 "ecological corridors",
                 "ecological security pattern"
                 ]

#"OthersDigitalModelling",
others_digitalmodeling=["moran's i statistic",
 'simulations, monte carlo framework',
 'invest urban cooling model',
 'megacity region spatial model',
 'statistical simulation: a tree-regression approach,',
 'change, scenario',
 'digital elevation models',
 'scenarios',
 '3d model',
 'mathemtical, heat-maps',
 'a cfd tool was used-the envi-met',
 'statistical, mathematical  random forest (rf), self-organizing map (som), and artificial neural network (ann) techniques to assess water demand patterns',
 'satistical: mono-window algorithm and buffer, correlation and regression analyses',
 'staistical',
 'forecasting',
 'mathematical, visual programming tools',
 'ahp, mcda',
 'statistical: logistic-regression',
 'random forest',
 'hydrological: the storm water management model (pcswmm)',
 'the statistical regression and physical model regression',
 'bayesian network modeling, decision support system',
 'the parallelized large eddy simulation (les) model palm',
 "'random forest' machine-learning model",
 'simulation, the reynolds-averaged navier-stokes based dispersion model',
 'nalytic hierarchy process (ahp)-based fuzzy evaluation',
 'scenario evaluation',
 'computational fluid dynamics',
 'solim model',
 'predictive models',
 'cellular automata model',
 'dance4water modeling approach',
 '3d computational fluid dynamics (cfd)',
 'climatic simulation: citysim',
 'chemistry-climate modelling system meco(n)',
 'the decision-making process',
 'statistical, hot spots,  binary logistic regression (blr) model',
 'hydrological: invest model',
 "geographically weighted regression (gwr), the bivariate moran's i index",
 'statistical: bivariate regressions',
 'mcda',
 '3d/ background computer generated animations (cga)',
 'change modeling, trend analysis, forecasting',
 'optimization',
 "digital surface model (dsm), python's tensorflow library; bresenham's line drawing algorithm",
 'climatic: envi-met software simulations',
 'climatic, statistical',
 'coupling modeling; urban carrying capacity coupling model (ucccm)',
 'regression models',
 'arcgis for spatial analysis and scs (soil conservation service) hydrological model simulation',
 'clumondo land-change model',
 'predicting land use, genetic agoritm',
 'landsupport gui',
 'the random forest algorithm',
 '3d lod1 and lod2 3d city model',
 'simulations: a simulator (called limulator 4.0) for als data',
 '3d',
 'climatic: dart',
 'the future land use simulation (flus)',
 '3d modeling, clustering',
 'cluster analysis;pca',
 'scenario',
 'suitability spatial assessment model, scenario',
 'mathematical:python',
 '3d urban model/citygml models (ogc standards)',
 'mathematical, markov processes',
 'template matching',
 'inverse weighted average method',
 'city information model; geobim',
 '3d photogrammetry modeling',
 'climatic, 3d',
 'hydrological: modeled cerp restoration scenarios',
 'predicting',
 'fuzzy multi-criteria evaluation',
 'arbon emission calculation and simulation to be used in softwares based on the level of accuracy and nature of their sources',
 'statistical logistic regression model',
 'envision tomorrow',
 'new benchmark functions for bound-constrained single-objective optimization that are based on a zigzag function',
 'statistical: logistic regression',
 'climatic performance',
 'statistical modeling, heuristic search algorithm',
 'dim: digital information model',
 'the numerical simulations were performed using urans (unsteady reynolds-averaged navier-stokes) equations and the kappa-omega sst model',
 'a stochastic sequential simulation',
 'gaussian mixture model',
 'structural equation modeling method',
 'ward clustering algorithm',
 'computational planning support systems',
 'dit - digital terrain modeling; geo-statistics',
 'climatic-envi-met',
 'hydrological',
 'spatial modelling',
 'dsm digital surface model',
 "geospatial and shannon's entropy techniques",
 '3d steady-state reynolds-averaged navier-stokes simulations are performed',
 'applied urban model',
 'the cubist (cb) and quantile random forest (qrf) models',
 'digital surface model (dsm)',
 'mcda, dematel',
 'random forest regression modelling',
 'scenario, newdepomo',
 'climatic conditions simulations vs planning scenarios',
 'simulations the pollutants emissions, diffusions, transportation, and pollution sources in specific areas',
 'statistical: regression model',
 'simulations: simulation decomposition',
 'analytical hierarchy, decision tree',
 'hydrological, statistical',
 'the computational fluid dynamics (cfd) approach',
 'mathematical/statistical',
 '3d microclimatic model in envi-met is used to simulate a misting system installed in rome',
 'cellular-automaton model, flus',
 'mathematical; hydrological',
 'digital surface model (dsm), visible-band difference vegetation index (vdvi)',
 'dijkstra and floyd–warshall algorithms',
 'ststistical/mathematical: longitudinal distribution model',
 'terrset software; decision forest-markov chain model in the land change modeller (lcm) tool;',
 'scenaio modeling',
 'statistical corelations',
 'improved potential model;(ipm)',
 'digital surface models',
 'bayesian additive regression tree model hybridized with a genetic algorithm',
 'fuzzy logic',
 'pedestrian simulation, a social-force model',
 'ca-markov-flus model, scenario simulation',
 'a random forest algorithm',
 'statistical/mathematcal',
 'time series. temporal prediction',
 'multiple regression model',
 'scenarios, mcda',
 'statistucal, cellular automata',
 'spatio-temporal analysis',
 'swmm',
 'cellular automata; scenarios',
 'decision support system',
 'random forest regression',
 'cellular-automata;  the flus model, simulation, scenarios',
 'predicting esp-flus model',
 'predicting; statistical, mathematical, nas algorithm',
 "hansen's gravitation model",
 'microsimulation;social force model;',
 'modeling the urban intersection form',
 'statistical: multi-level regression models and joint-significance mediation tests',
 'simulations: htb2 and the virvil plugin',
 'generalized additive and land-use changes modeling;the total nitrogen and phosphorus concentrations model',
 'computational fluid dynamics (cfd',
 'clustering algorithms: k-means and agglomerative hierarchical clustering',
 'mcda, logic scoring of preference',
 'universal soil loss equation (usle)',
 'spatial multicriteria evaluation',
 'mathematica/ststistical simulations: monte carlo simulation',
 'biophysical modeling',
 'mcda: fuzzy-ahp, srs and rsw weightage',
 'clustering',
 'multiscale geographically weighted regression (mgwr)',
 'mathemeatical',
 'random forests (rf)',
 'spatial model of flooding using the rational modification method',
 'the conefor model',
 'simulate multiple least cost corridors (mlcc)',
 'monte carlo simulation',
 'hydraulic models; the epa-swmm',
 'the envi-met and energyplus models',
 'causal inference',
 'hydrological modeling',
 'multicriteria evaluation',
 'ls models, the rf-reptree model',
 'statistical/beam-, slab- or 3d-models',
 'simulations, land cover change model terrset to project future land cover from 2016 to 2040',
 'the multicriteria decision support methodology-constructivist (mcda-c)',
 'geospatial modelling, citygml 2.0',
 'a spatial gray-level co-occurrence matrix model',
 'envi-met; climatic; the optimization of gi',
 'clustering algorithms',
 'fluid dynamics simulations',
 'the gpc model, the gaussian process classification (gpc) and the improved weight-based generalized objective function',
 'statistics',
 'cellular automata markov chain model, simulation',
 '3d modeling, geological',
 'green infrastructure spatial planning (gisp) model',
 'hydrolgical, simulations',
 'statistical: spatial durbin model',
 '3d city modelling; ca (cellular automata) model; sleuth',
 'statistical, spatiotemporal analysis',
 'multivariate regression',
 'cellular-automata',
 'simulation, predicting',
 'decision-making support tools',
 '3d city models',
 'virtual landscapes to model interactions, simulations',
 'digital model',
 'mathematical: land optimization;  multi-objective integer linear optimization; multi-objective integer linear program',
 'envi-met microclimate simulation tool',
 '3-d digital modeling technology',
 'graph;network theory, visibility graph analysis (vga)',
 'different performance simulation tools (i.e. envi-met, trnsys, ladybug/honeybee, citysim, and solene-microclimat)',
 'clustering, network kernel density visualization alternatives: ggregate distance augmentation (ada), interval augmentation (ia), and hybrid augmentation (ha)',
 'general landscape connectivity model (glcm)',
 '3d modeling; agent based modeling (abm)',
 'geoststistical',
 'mathematical model',
 'statistical: generalized linear model',
 'modified sintacs model',
 'three-dimensional digital participatory planning (3ddpp)',
 'simulation-optimization model (s-o model)',
 'statistical: hierarchical bayesian modeling, using markov chain monte carlo simulation',
 'mathematical, modeling, cfd simulations',
 'mcdm',
 'soundscape analysis',
 '(1) geometric modelling by parametric modelling tools; (2) simulation of environmental parameters by using bps tools; (3) shape optimization by using an evolutionary algorithm;',
 'integrated socio‐ecological modelling',
 'cellular automata (ca)',
 'ststistical',
 'mathematical: lotka-volterra mathematical model; scenario',
 'urban high-density green space energy-saving planning model',
 'mca/mcda',
 'high-resolution digital elevation models (dems)',
 'digital elevation model (dem)',
 'ahp, mcdm',
 'combination least cost and circuit models',
 'economic input-output model, planning support systems',
 'logistic regression (lr) analysis',
 'statistical-method not provided',
 'geospatial simulation',
 'performance simulation',
 'pm2.5 concentration prediction model',
 'three-dimensional modelling; visual programming language techniques',
 'simulations',
 'integrating grey markov model and future land use simulation (flus)',
 'climatic simulations',
 'a clustering-based algorithm to identify aoes and compare it to another method, the geographical interpolation of endemism, based on a kernel density approach',
 'statistical: entropy landscape metrics',
 'spatial multicriteria evaluation, ahp, landslides model',
 'the icona erosion risk method',
 'geostatistics, monte carlo simulation',
 'model of development',
 'optimization, mcda, promethee;ahp',
 '3d modeling',
 'statistical: the markov two-step switching regime regression model',
 'mathematical:kalman filters',
 'agent-based modelling (abm)',
 'mcda, ahp',
 'digital elevation model',
 'statistical, multi-regression analysis',
 'mathematical',
 '3d computational fluid dynamics (cfd) simulations of airflow and pollutant dispersion',
 'statistical',
 'spatiotemporal modeling',
 'optimal city planning model',
 'the city geography markup language (citygml)',
 'system dynamics',
 'simulation; markov chain model',
 'simulation, transformation analysis and kernel density analysis to study the spatial and temporal characteristics',
 'matheatical:pollutant dispersion',
 'scenario/future/statistical modeling',
 'geographically weighted regression',
 'computational fluid dynamics technique; the unsteady reynolds-averaged navier-stokes equations and the kappa-omega sst turbulence model for the numerical simulations',
 'cellular automata',
 'numerical simulations,  mesonh-surfex-teb mesoscale atmospheric model',
 '3d modelling',
 'a parametric modelling approach',
 'a random forest modeling framework',
 'mcda, cilmatic',
 'multiple linear regression;random forest',
 'smart city design models',
 'aerosol retrieval algorithm']


gis=["gis","toolsoftware","gisalgorithms","arcgis"," gis", "4dgis", "gis4d",
     "geographic information","geographical information","interactive map",
     "geoinformation","getis-ord","geo spatial technology","geospatial technology","geo-ict",
     "geospatial information and communication technology","bim-gis",
     "map algebra","spatial information systems","sis","geotopsis",
     "geospatial web-based platform","web-gis","geospatial techniques"]
#"OthersGIS",
others_gis=['space syntax',
 'the conventional god and the ahp-driven godl algorithms',
 '3d isovist;voxel',
 'geodesign',
 'esda',
 'volunteered geographic information (vgi)',
 'pgis',
 'the statistical regression and physical model regression',
 'open source gis based tool',
 'geotechnologies',
 'geovisualisation',
 'the geodetector method',
 'geographically weighted regression (gwr) models',
 '"cluenda" (new tool specifically developed is in gis',
 'geolocation',
 'network geographic information system',
 'spatial syntax',
 'vertical voxel viewsheds',
 'webgis communication technology',
 'he gahpsort ii method',
 'crowdsourcing',
 'compatibility with other tools',
 'spatial regression analyses',
 'drastic method',
 'geoprocessing techniques',
 'ppgis',
 'participatory geographic information systems (pgis)',
 'ppgis applications',
 'data, geodatabase']


#Manufactoring
n3dPrinting=["3dprinting"]
cam=["cam"]
manufactoring=["manufactoring"]
#"OthersManufactoring",
others_manufactoring=[]

#"Robotic",
dron=["dronuav/uas","dron","uav","uas"," dron"]
robotic=["robotic","autonomous vehicles","robot"]
#"OthersRobotic",
others_robotic=['agricultural robots',
 'remotely piloted aircraft',
 'remotely piloted aircraft-rpa',
 'tls/ mobile robot',
 'automated vehicles',
 'a remotely operated vehicle (rov)']

iot=["iot","edge computing","internet of things","smart city","smart cities"] #smart cities?
#"Algorithms",
mobile_phoneapps=["mobile phone apps","mobile apps","smartphone"]
web_platforms=["web platform","web platforms"," web","online"]
#Patch-Generating Land Use Simulation
pc_cloud=["software"]
#"OtherPCCloud",
#other_algorithms=["algorithm","algorithms"]
#"OtherAlgorithms",
others_algorithms=['space syntax',
 'coklimax',
 'selective nonlocal resunext++ (snlrux++)',
 'citysim',
 'unity environment',
 'accessible to stakeholders through a web-based pss',
 'geodetector',
 'gama platform',
 'copert',
 'open-source gis',
 'openfoam',
 'viswalk',
 'street view imges',
 'hot spot (getis-ord gi*)',
 'landsupport',
 'the flus model',
 'algorithm, called sherloc',
 'decision support system indimar',
 'surfer 13 software, google earth',
 'terrset v.18 software',
 'envision tomorrow',
 'blazegraph™, citygml 2.0, the ontocitygml tbox',
 'models: global climate models, storm water menagement model, chesapeake bay land change model (cblcm)',
 'google street view street audit tool',
 'pyspark',
 'its applications review',
 'citygml, 3d bag',
 'the msp challenge',
 'the modular toolset invest (integrated valuation of ecosystem services and tradeoffs)',
 'envi-met, fulcrum mobile application',
 'webvr technology',
 'invest',
 'envi-met',
 'the land.info design tool dss',
 'openstreetmap',
 'software review',
 "noaa's satellite and information services (nesdis)",
 'houdini',
 'unity3d',
 'an interactive 3ddpp tool was employed',
 'urban atlas, the conefor model',
 'swmm',
 'an algorithm for the point placement , a program utility by python programming  language',
 'arcgis 10.4 environment',
 'flus model',
 'nsdi tools',
 'arcgis',
 'envi-met program',
 'walk score',
 'envi-met, trnsys, ladybug/honeybee, citysim, and solene-microclimat',
 'invest tools',
 'the envi-met and energyplus models',
 'lightgbm',
 'the cockpit social infrastructure',
 'google earth',
 'street view',
 'ai4geo',
 'gis platform',
 'densenet169',
 'cityscope',
 'envi-met v4',
 'openstreetmap, osmnx',
 'terrset software',
 'envi 5.5 software',
 'open-source system called eimage',
 'getis-ord gi*',
 'online user generated content,  a state-of-the-art natural language processing network (bert)',
 'open street maps',
 'lscorridors to simulate multiple least cost corridors (mlcc)',
 'spatial syntax, webgis communication technology',
 'web3d viewer, citygml',
 'google earth engine, land-use change simulation, flus',
 'fragstats software',
 'arcgis10.5 software',
 'open source software, taal open lidar data, open street map',
 'sentiment analysis',
 'cfd simulations',
 'super decision software',
 'palm - the parallelized large eddy simulation (les) model palm',
 'refined dse-linknet, deepglobe road extraction challenge',
 'rhinoceros three-dimensional software, and grashopper3d',
 'spatial syntax',
 'rosetrajvis',
 'urban cfd software',
 'the flus model was made into gui software named geosos-flus',
 'maxent model',
 'rhino3d cad',
 'ergo lab data platform',
 'the city geography markup language (citygml)',
 'space syntax approach',
 'walk score®',
 'spot 6 image',
 'super decision version 3.2 software']


others_web=['flus model',
 'nsdi tools',
 'coklimax',
 'decision support system indimar',
 'walk score',
 'surfer 13 software, google earth',
 'envision tomorrow',
 'accessible to stakeholders through a web-based pss',
 'open source software, taal open lidar data, open street map',
 'sentiment analysis',
 'lightgbm',
 'the cockpit social infrastructure',
 'google street view street audit tool',
 'pyspark',
 'google earth',
 'citygml, 3d bag',
 'street view',
 'gama platform',
 'copert',
 'ai4geo',
 'gis platform',
 'the msp challenge',
 'cityscope',
 'spatial syntax',
 'openstreetmap, osmnx',
 'street view imges',
 'webvr technology',
 'invest',
 'ergo lab data platform',
 'walk score®',
 'the land.info design tool dss',
 'spot 6 image',
 'landsupport',
 'openstreetmap',
 'open street maps',
 'online user generated content,  a state-of-the-art natural language processing network (bert)',
 "noaa's satellite and information services (nesdis)",
 'spatial syntax, webgis communication technology',
 'web3d viewer, citygml',
 'an interactive 3ddpp tool was employed',
 'google earth engine, land-use change simulation, flus',
 'urban atlas, the conefor model']

other_technologies=["technology","technologies"]
#"OTHER TECHNOLOGIES",


gps=["gps","global positioning system"] #+gnss
gnss=["gnss","global navigation satellite system"]
ict=["ict","icts","wireless network","wifi","wi-fi","mobile devices","geo-ict"]

blockchain=["blockchain"]
n5gbeyond=["5G/Beyond","5G"]
cloud=["cloud"]               #not CLOUD REMOVAL
gamification=["gamification","game"]
devices=["eye-tracking devices","smart cap",
         "eye tracking",
"smart glove",
"thermometer",
"pedometer",
"accelerometer",
"mobile monitoring",
"camera",
"video tracking",
"smartphone",
"smartphone's hygrometer",
"light sensor",
"module",
"laser component and lidar data generation",
"leap motion hardware","hardware",
"sensors",
"wearable",
"photovoltaic",
"mobile monitoring"]


tech_column_name_to_keywords = {
 "Technology":list(set(cad+data_science+data_minig+big_data+crowdsourcing+open_data+others_data+vr+
                       ai_related+
                       deep_learning+artificial_inteligence+machine_learning+mas+others_ai+
                       lidar+remote_sensing+others_rs+
                       social_networks+social_news+blogging+bookmarking+media_sharing+others_socialmedia+
                       bim+sim+lim+pointcloud+rendering+n3dscaning+statistical_modeling+n3dModelling+
                       mcda+pss_dss+hydrological+other_modelling+others_digitalmodeling+
                       gis+others_gis+n3dPrinting+cam+manufactoring+others_manufactoring+
                       dron+robotic+others_robotic+iot+mobile_phoneapps+web_platforms+pc_cloud+
                       others_algorithms+
                       other_technologies+gps+gnss+ict+blockchain+n5gbeyond+cloud+gamification+devices)),   
"CAD":cad,
"Data":list(set(data_science+data_minig+big_data+open_data+crowdsourcing+others_data)),
"Data science":data_science+others_data_data_science,
"Data mining":data_minig+others_data_data_minig,
"Big data":big_data+others_data_big_data,
"Crowdsourcing":crowdsourcing+others_data_crowdsourcing,
"Open data":open_data+others_data_open_data,
#"OthersData":[],
"AI&related":list(set(ai_related+deep_learning+artificial_inteligence+machine_learning+mas+others_ai)),
"Deep Learning":deep_learning,
"Artificial Intelligence":artificial_inteligence,
"Machine learning":list(set(deep_learning+artificial_inteligence+machine_learning)),




"MAS":mas,
#"OthersAI":[],
"Remote sensing":list(set(remote_sensing+lidar+others_rs)),
"Lidar":lidar,
#"OthersRS":[],
"Social Media":list(set(socialmedia+social_networks+social_news+blogging+bookmarking+media_sharing+others_socialmedia)),
"SocialNetworks":social_networks,
"SocialNews":social_news,
"Blogging":blogging,
"Bookmarking":bookmarking,
"MediaSharing":media_sharing,
#"OthersSocialMedia":other_socialmedia,
"VR/AR/MR":vr,
"VR":["vr","virtual reality","virtual environments","cave2","cave"],
"AR":["ar","augmented reality","diminished reality"],
"MR":["mr","mixed reality"],
"DigitalModelling":list(set(bim+sim+lim+pointcloud+rendering+n3dscaning+statistical_modeling+n3dModelling+
                            mcda+pss_dss+hydrological+other_modelling+others_digitalmodeling)),
"BIM":bim,
"SIM":sim,
"LIM":lim,
"PointCloud":pointcloud,
"Rendering":rendering,
"3dScanning":n3dscaning,
"Statistical modelling":statistical_modeling,
"3dModelling":n3dModelling,
"MCDA/AHP":mcda,
"PSS/DSS":pss_dss,
"HydrologicalModel":hydrological,
"ConnectivityModels":conectivity,
"ClimaticModel":climatic,
#"OthersDigitalModelling":other_modelling,
"GIS":gis+others_gis,
"ToolsSoftware":["toolsoftware"],
"GISAlgorithms":["gisalgorithms"],
#"OthersGIS":[],
"Manufactoring":list(set(manufactoring+n3dPrinting+cam)),
"3dPrinting":n3dPrinting,
"CAM":cam,
"OthersManufactoring":[],
"Robotic":robotic+dron+others_robotic,
"DronUAV/UAS":dron,
#"OthersRobotic":[],
"IoT":iot,
"Algorithms":list(set(mobile_phoneapps+web_platforms+pc_cloud+others_algorithms)),
"MobilePhoneApps":mobile_phoneapps,
"WebPlatforms":web_platforms+others_web,
#"OtherPCCloud":pc_cloud,
#"OtherAlgorithms":other_algorithms,
#"OTHER TECHNOLOGIES":other_technologies,
"Literature review":["literature review"],
"GPS":gps,
"GNSS":gnss,
"ICT":ict,
"Blockchain":blockchain,
"5G/Beyond":n5gbeyond,
"Cloud":cloud,
"Gamification":gamification,
"Devices":devices,
"MCDA/PSS":mcda+pss_dss,
"allICT":list(set(iot+gps+gnss+ict+blockchain+n5gbeyond+cloud+gamification+devices)),
"all3dmodeling":list(set(bim+lim+pointcloud+rendering+n3dscaning+n3dModelling)),

}


'''-----------------technology detection --------------'''
tp,tn,fp,fn = defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)
rfp,rfn = defaultdict(list),defaultdict(list)
 
for index, row in filtered.iterrows():
    abstract=row["Abstract"].lower()
    kw = row["Keywords"]
    title = row["Title"].lower()
    try:    
        kw = ' '.join([w for w in kw.split(';') if not kw.isnumeric()]).lower()
        abstract='{} {} {}'.format(abstract,kw,title)
        abstract=re.sub(r'[^a-zA-Z0-9\s]', "", abstract)

    except:
        abstract='{} {}'.format(abstract,title)
        abstract=re.sub(r'[^a-zA-Z0-9\s]', "", abstract)

    
    for t,k in tech_column_name_to_keywords.items():    
        
        tech_keywords = []

        for klucz in k:

            klucz = re.sub(r'[^a-zA-Z0-9\s]', "", klucz)
            if " " in klucz:
                if klucz in abstract:
                    tech_keywords.extend(klucz)
            else:
                if klucz in abstract.split():
                    tech_keywords.extend(klucz)
            klucz = '{}s'.format(klucz)
            if " " in klucz:
                if klucz in abstract:
                    tech_keywords.extend(klucz)
            else:
                if klucz in abstract.split():
                    tech_keywords.extend(klucz)
                    
        #if (row["Record Number"]==5029.0) and (t=="ICT"):
        #    print(tech_keywords)        
        
        if (len(tech_keywords)>0):
            filtered.at[filtered["Record Number"]==row["Record Number"],t]='True'
        else:
            filtered.at[filtered["Record Number"]==row["Record Number"],t]='False'
#filtered['Temathic_not_ai_or_ds'] = ((filtered['ClimaticModel']=='True') | (filtered['HydrologicalModel']=='True') | (filtered['ConnectivityModels']=='True')) & (filtered['AI&related']=='False') & (filtered['MCDA/AHP']=='False') & (filtered['PSS/DSS']=='False')
#filtered['Stat_not_tema_or_ai_or_ds'] = (filtered['Statistical modelling']=='True') & (filtered['ClimaticModel']=='False') & (filtered['HydrologicalModel']=='Fale') & (filtered['ConnectivityModels']=='False') & (filtered['AI&related']=='False') & (filtered['MCDA/AHP']=='False') & (filtered['PSS/DSS']=='False')
#filtered['Stat_not_ai_or_ds'] = (filtered['Statistical modelling']=='True') & (filtered['AI&related']=='False') & (filtered['MCDA/AHP']=='False') & (filtered['PSS/DSS']=='False')


filtered.replace({False: 0, True: 1}, inplace=True)
filtered.replace({"False": 0, "True": 1}, inplace=True)    

filtered['Temathic_not_ai_or_ds'] = ((filtered['ClimaticModel']==1) | (filtered['HydrologicalModel']==1) | (filtered['ConnectivityModels']==1)) & (filtered['AI&related']==0) & (filtered['MCDA/AHP']==0) & (filtered['PSS/DSS']==0)
filtered['Stat_not_tema_or_ai_or_ds'] = (filtered['Statistical modelling']==1) & (filtered['ClimaticModel']==0) & (filtered['HydrologicalModel']==0) & (filtered['ConnectivityModels']==0) & (filtered['AI&related']==0) & (filtered['MCDA/AHP']==0) & (filtered['PSS/DSS']==0)
filtered['Stat_not_ai_or_ds'] = (filtered['Statistical modelling']==1) & (filtered['AI&related']==0) & (filtered['MCDA/AHP']==0) & (filtered['PSS/DSS']==0)
filtered['Cloud'] = ((filtered['Cloud']==1) & (filtered['PointCloud']==0))
filtered['Other Digital Modelling'] = filtered['Stat_not_ai_or_ds']
filtered['OthersData'] = ((filtered['Data']==1) & (filtered['Data science']==0) & (filtered['Data mining']==0) & (filtered['Big data']==0) & (filtered['Crowdsourcing']==0) & (filtered['Open data']==0))
filtered['OthersAI'] = ((filtered['AI&related']==1) & (filtered['Deep Learning']==0) & (filtered['Artificial Intelligence']==0) & (filtered['Machine learning']==0) & (filtered['MAS']==0))
filtered['allICT'] = ((filtered['allICT']==1) & (filtered['PointCloud']==0))

filtered.replace({False: 0, True: 1}, inplace=True)
filtered.replace({"False": 0, "True": 1}, inplace=True)    


filtered.to_excel('C:/ProjektyPython/textClasification/output/ALL PAPERS MAY10_processed_12112023.xlsx',index=False)
'''
ręcznie dodano kolumnę Other Digital Modelling, która jest tożsama z Stat_not_ai_or_ds
ręcznie uzupełniono kolumnę OthersData, Data=1, pozostałe Dataxxx=0
trzeba odfiltrować rekordy bez podanego roku
'''


