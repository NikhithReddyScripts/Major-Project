import telebot
import numpy as np
import yfinance as yf
import datetime
import time
import statistics
from newsapi import NewsApiClient
from textblob import TextBlob
from requests import get
from urllib.parse import quote_plus

nifty_500_dict ={
 '360 one wam ltd.': '360ONE',
 '3m india ltd.': '3MINDIA',
 'abb india ltd.': 'ABB',
 'acc ltd.': 'ACC',
 'aia engineering ltd.': 'AIAENG',
 'apl apollo tubes ltd.': 'APLAPOLLO',
 'au small finance bank ltd.': 'AUBANK',
 'aarti drugs ltd.': 'AARTIDRUGS',
 'aarti industries ltd.': 'AARTIIND',
 'aavas financiers ltd.': 'AAVAS',
 'abbott india ltd.': 'ABBOTINDIA',
 'adani energy solutions ltd.': 'ADANIENSOL',
 'adani enterprises ltd.': 'ADANIENT',
 'adani green energy ltd.': 'ADANIGREEN',
 'adani ports and special economic zone ltd.': 'ADANIPORTS',
 'adani power ltd.': 'ADANIPOWER',
 'adani total gas ltd.': 'ATGL',
 'adani wilmar ltd.': 'AWL',
 'aditya birla capital ltd.': 'ABCAPITAL',
 'aditya birla fashion and retail ltd.': 'ABFRL',
 'aegis logistics ltd.': 'AEGISCHEM',
 'aether industries ltd.': 'AETHER',
 'affle (india) ltd.': 'AFFLE',
 'ajanta pharmaceuticals ltd.': 'AJANTPHARM',
 'alembic pharmaceuticals ltd.': 'APLLTD',
 'alkem laboratories ltd.': 'ALKEM',
 'alkyl amines chemicals ltd.': 'ALKYLAMINE',
 'allcargo logistics ltd.': 'ALLCARGO',
 'alok industries ltd.': 'ALOKINDS',
 'amara raja energy & mobility ltd.': 'ARE&M',
 'amber enterprises india ltd.': 'AMBER',
 'ambuja cements ltd.': 'AMBUJACEM',
 'angel one ltd.': 'ANGELONE',
 'anupam rasayan india ltd.': 'ANURAS',
 'apar industries ltd.': 'APARINDS',
 'apollo hospitals enterprise ltd.': 'APOLLOHOSP',
 'apollo tyres ltd.': 'APOLLOTYRE',
 'aptus value housing finance india ltd.': 'APTUS',
 'archean chemical industries ltd.': 'ACI',
 'asahi india glass ltd.': 'ASAHIINDIA',
 'ashok leyland ltd.': 'ASHOKLEY',
 'asian paints ltd.': 'ASIANPAINT',
 'aster dm healthcare ltd.': 'ASTERDM',
 'astral ltd.': 'ASTRAL',
 'atul ltd.': 'ATUL',
 'aurobindo pharma ltd.': 'AUROPHARMA',
 'avanti feeds ltd.': 'AVANTIFEED',
 'avenue supermarts ltd.': 'DMART',
 'axis bank ltd.': 'AXISBANK',
 'beml ltd.': 'BEML',
 'bls international services ltd.': 'BLS',
 'bse ltd.': 'BSE',
 'bajaj auto ltd.': 'BAJAJ-AUTO',
 'bajaj finance ltd.': 'BAJFINANCE',
 'bajaj finserv ltd.': 'BAJAJFINSV',
 'bajaj holdings & investment ltd.': 'BAJAJHLDNG',
 'balaji amines ltd.': 'BALAMINES',
 'balkrishna industries ltd.': 'BALKRISIND',
 'balrampur chini mills ltd.': 'BALRAMCHIN',
 'bandhan bank ltd.': 'BANDHANBNK',
 'bank of baroda': 'BANKBARODA',
 'bank of india': 'BANKINDIA',
 'bank of maharashtra': 'MAHABANK',
 'bata india ltd.': 'BATAINDIA',
 'bayer cropscience ltd.': 'BAYERCROP',
 'berger paints india ltd.': 'BERGEPAINT',
 'bharat dynamics ltd.': 'BDL',
 'bharat electronics ltd.': 'BEL',
 'bharat forge ltd.': 'BHARATFORG',
 'bharat heavy electricals ltd.': 'BHEL',
 'bharat petroleum corporation ltd.': 'BPCL',
 'bharti airtel ltd.': 'BHARTIARTL',
 'bikaji foods international ltd.': 'BIKAJI',
 'biocon ltd.': 'BIOCON',
 'birla corporation ltd.': 'BIRLACORPN',
 'birlasoft ltd.': 'BSOFT',
 'blue dart express ltd.': 'BLUEDART',
 'blue star ltd.': 'BLUESTARCO',
 'bombay burmah trading corporation ltd.': 'BBTC',
 'borosil renewables ltd.': 'BORORENEW',
 'bosch ltd.': 'BOSCHLTD',
 'brigade enterprises ltd.': 'BRIGADE',
 'brightcom group ltd.': 'BCG',
 'britannia industries ltd.': 'BRITANNIA',
 'c.e. info systems ltd.': 'MAPMYINDIA',
 'ccl products (i) ltd.': 'CCL',
 'cesc ltd.': 'CESC',
 'cg power and industrial solutions ltd.': 'CGPOWER',
 'cie automotive india ltd.': 'CIEINDIA',
 'crisil ltd.': 'CRISIL',
 'csb bank ltd.': 'CSBBANK',
 'campus activewear ltd.': 'CAMPUS',
 'can fin homes ltd.': 'CANFINHOME',
 'canara bank': 'CANBK',
 'capri global capital ltd.': 'CGCL',
 'carborundum universal ltd.': 'CARBORUNIV',
 'castrol india ltd.': 'CASTROLIND',
 'ceat ltd.': 'CEATLTD',
 'central bank of india': 'CENTRALBK',
 'central depository services (india) ltd.': 'CDSL',
 'century plyboards (india) ltd.': 'CENTURYPLY',
 'century textile & industries ltd.': 'CENTURYTEX',
 'cera sanitaryware ltd': 'CERA',
 'chalet hotels ltd.': 'CHALET',
 'chambal fertilizers & chemicals ltd.': 'CHAMBLFERT',
 'chemplast sanmar ltd.': 'CHEMPLASTS',
 'cholamandalam financial holdings ltd.': 'CHOLAHLDNG',
 'cholamandalam investment and finance company ltd.': 'CHOLAFIN',
 'cipla ltd.': 'CIPLA',
 'city union bank ltd.': 'CUB',
 'clean science and technology ltd.': 'CLEAN',
 'coal india ltd.': 'COALINDIA',
 'cochin shipyard ltd.': 'COCHINSHIP',
 'coforge ltd.': 'COFORGE',
 'colgate palmolive (india) ltd.': 'COLPAL',
 'computer age management services ltd.': 'CAMS',
 'concord biotech ltd.': 'CONCORDBIO',
 'container corporation of india ltd.': 'CONCOR',
 'coromandel international ltd.': 'COROMANDEL',
 'craftsman automation ltd.': 'CRAFTSMAN',
 'creditaccess grameen ltd.': 'CREDITACC',
 'crompton greaves consumer electricals ltd.': 'CROMPTON',
 'cummins india ltd.': 'CUMMINSIND',
 'cyient ltd.': 'CYIENT',
 'dcm shriram ltd.': 'DCMSHRIRAM',
 'dlf ltd.': 'DLF',
 'dabur india ltd.': 'DABUR',
 'dalmia bharat ltd.': 'DALBHARAT',
 'data patterns (india) ltd.': 'DATAPATTNS',
 'deepak fertilisers & petrochemicals corp. ltd.': 'DEEPAKFERT',
 'deepak nitrite ltd.': 'DEEPAKNTR',
 'delhivery ltd.': 'DELHIVERY',
 'delta corp ltd.': 'DELTACORP',
 'devyani international ltd.': 'DEVYANI',
 "divi's laboratories ltd.": 'DIVISLAB',
 'dixon technologies (india) ltd.': 'DIXON',
 'dr. lal path labs ltd.': 'LALPATHLAB',
 "dr. reddy's laboratories ltd.": 'DRREDDY',
 'e.i.d. parry (india) ltd.': 'EIDPARRY',
 'eih ltd.': 'EIHOTEL',
 'epl ltd.': 'EPL',
 'easy trip planners ltd.': 'EASEMYTRIP',
 'eicher motors ltd.': 'EICHERMOT',
 'elgi equipments ltd.': 'ELGIEQUIP',
 'emami ltd.': 'EMAMILTD',
 'endurance technologies ltd.': 'ENDURANCE',
 'engineers india ltd.': 'ENGINERSIN',
 'epigral ltd.': 'EPIGRAL',
 'equitas small finance bank ltd.': 'EQUITASBNK',
 'eris lifesciences ltd.': 'ERIS',
 'escorts kubota ltd.': 'ESCORTS',
 'exide industries ltd.': 'EXIDEIND',
 'fdc ltd.': 'FDC',
 'fsn e-commerce ventures ltd.': 'NYKAA',
 'federal bank ltd.': 'FEDERALBNK',
 'fertilisers and chemicals travancore ltd.': 'FACT',
 'fine organic industries ltd.': 'FINEORG',
 'finolex cables ltd.': 'FINCABLES',
 'finolex industries ltd.': 'FINPIPE',
 'firstsource solutions ltd.': 'FSL',
 'five-star business finance ltd.': 'FIVESTAR',
 'fortis healthcare ltd.': 'FORTIS',
 'g r infraprojects ltd.': 'GRINFRA',
 'gail (india) ltd.': 'GAIL',
 'gmm pfaudler ltd.': 'GMMPFAUDLR',
 'gmr airports infrastructure ltd.': 'GMRINFRA',
 'galaxy surfactants ltd.': 'GALAXYSURF',
 'general insurance corporation of india': 'GICRE',
 'gillette india ltd.': 'GILLETTE',
 'gland pharma ltd.': 'GLAND',
 'glaxosmithkline pharmaceuticals ltd.': 'GLAXO',
 'glenmark life sciences ltd.': 'GLS',
 'glenmark pharmaceuticals ltd.': 'GLENMARK',
 'global health ltd.': 'MEDANTA',
 'go fashion (india) ltd.': 'GOCOLORS',
 'godawari power & ispat ltd.': 'GPIL',
 'godfrey phillips india ltd.': 'GODFRYPHLP',
 'godrej consumer products ltd.': 'GODREJCP',
 'godrej industries ltd.': 'GODREJIND',
 'godrej properties ltd.': 'GODREJPROP',
 'granules india ltd.': 'GRANULES',
 'graphite india ltd.': 'GRAPHITE',
 'grasim industries ltd.': 'GRASIM',
 'great eastern shipping co. ltd.': 'GESHIP',
 'grindwell norton ltd.': 'GRINDWELL',
 'gujarat alkalies & chemicals ltd.': 'GUJALKALI',
 'gujarat ambuja exports ltd.': 'GAEL',
 'gujarat fluorochemicals ltd.': 'FLUOROCHEM',
 'gujarat gas ltd.': 'GUJGASLTD',
 'gujarat narmada valley fertilizers and chemicals ltd.': 'GNFC',
 'gujarat pipavav port ltd.': 'GPPL',
 'gujarat state fertilizers & chemicals ltd.': 'GSFC',
 'gujarat state petronet ltd.': 'GSPL',
 'h.e.g. ltd.': 'HEG',
 'hcl technologies ltd.': 'HCLTECH',
 'hdfc asset management company ltd.': 'HDFCAMC',
 'hdfc bank ltd.': 'HDFCBANK',
 'hdfc life insurance company ltd.': 'HDFCLIFE',
 'hfcl ltd.': 'HFCL',
 'hle glascoat ltd.': 'HLEGLAS',
 'happiest minds technologies ltd.': 'HAPPSTMNDS',
 'havells india ltd.': 'HAVELLS',
 'hero motocorp ltd.': 'HEROMOTOCO',
 'hindalco industries ltd.': 'HINDALCO',
 'hindustan aeronautics ltd.': 'HAL',
 'hindustan copper ltd.': 'HINDCOPPER',
 'hindustan petroleum corporation ltd.': 'HINDPETRO',
 'hindustan unilever ltd.': 'HINDUNILVR',
 'hindustan zinc ltd.': 'HINDZINC',
 'hitachi energy india ltd.': 'POWERINDIA',
 'home first finance company india ltd.': 'HOMEFIRST',
 'honeywell automation india ltd.': 'HONAUT',
 'housing & urban development corporation ltd.': 'HUDCO',
 'icici bank ltd.': 'ICICIBANK',
 'icici lombard general insurance company ltd.': 'ICICIGI',
 'icici prudential life insurance company ltd.': 'ICICIPRULI',
 'icici securities ltd.': 'ISEC',
 'idbi bank ltd.': 'IDBI',
 'idfc first bank ltd.': 'IDFCFIRSTB',
 'idfc ltd.': 'IDFC',
 'iifl finance ltd.': 'IIFL',
 'irb infrastructure developers ltd.': 'IRB',
 'ircon international ltd.': 'IRCON',
 'itc ltd.': 'ITC',
 'iti ltd.': 'ITI',
 'india cements ltd.': 'INDIACEM',
 'indiabulls housing finance ltd.': 'IBULHSGFIN',
 'indiamart intermesh ltd.': 'INDIAMART',
 'indian bank': 'INDIANB',
 'indian energy exchange ltd.': 'IEX',
 'indian hotels co. ltd.': 'INDHOTEL',
 'indian oil corporation ltd.': 'IOC',
 'indian overseas bank': 'IOB',
 'indian railway catering and tourism corporation ltd.': 'IRCTC',
 'indian railway finance corporation ltd.': 'IRFC',
 'indigo paints ltd.': 'INDIGOPNTS',
 'indraprastha gas ltd.': 'IGL',
 'indus towers ltd.': 'INDUSTOWER',
 'indusind bank ltd.': 'INDUSINDBK',
 'infibeam avenues ltd.': 'INFIBEAM',
 'info edge (india) ltd.': 'NAUKRI',
 'infosys ltd.': 'INFY',
 'ingersoll rand (india) ltd.': 'INGERRAND',
 'intellect design arena ltd.': 'INTELLECT',
 'interglobe aviation ltd.': 'INDIGO',
 'ipca laboratories ltd.': 'IPCALAB',
 'j.b. chemicals & pharmaceuticals ltd.': 'JBCHEPHARM',
 'j.k. cement ltd.': 'JKCEMENT',
 'jbm auto ltd.': 'JBMA',
 'jk lakshmi cement ltd.': 'JKLAKSHMI',
 'jk paper ltd.': 'JKPAPER',
 'jm financial ltd.': 'JMFINANCIL',
 'jsw energy ltd.': 'JSWENERGY',
 'jsw steel ltd.': 'JSWSTEEL',
 'jamna auto industries ltd.': 'JAMNAAUTO',
 'jindal saw ltd.': 'JINDALSAW',
 'jindal stainless ltd.': 'JSL',
 'jindal steel & power ltd.': 'JINDALSTEL',
 'jubilant foodworks ltd.': 'JUBLFOOD',
 'jubilant ingrevia ltd.': 'JUBLINGREA',
 'jubilant pharmova ltd.': 'JUBLPHARMA',
 'justdial ltd.': 'JUSTDIAL',
 'jyothy labs ltd.': 'JYOTHYLAB',
 'k.p.r. mill ltd.': 'KPRMILL',
 'kei industries ltd.': 'KEI',
 'knr constructions ltd.': 'KNRCON',
 'kpit technologies ltd.': 'KPITTECH',
 'krbl ltd.': 'KRBL',
 'ksb ltd.': 'KSB',
 'kajaria ceramics ltd.': 'KAJARIACER',
 'kalpataru projects international ltd.': 'KPIL',
 'kalyan jewellers india ltd.': 'KALYANKJIL',
 'kansai nerolac paints ltd.': 'KANSAINER',
 'karur vysya bank ltd.': 'KARURVYSYA',
 'kaynes technology india ltd.': 'KAYNES',
 'kec international ltd.': 'KEC',
 'kfin technologies ltd.': 'KFINTECH',
 'kotak mahindra bank ltd.': 'KOTAKBANK',
 'krishna institute of medical sciences ltd.': 'KIMS',
 'l&t finance holdings ltd.': 'L&TFH',
 'l&t technology services ltd.': 'LTTS',
 'lic housing finance ltd.': 'LICHSGFIN',
 'ltimindtree ltd.': 'LTIM',
 'lakshmi machine works ltd.': 'LAXMIMACH',
 'larsen & toubro ltd.': 'LT',
 'latent view analytics ltd.': 'LATENTVIEW',
 'laurus labs ltd.': 'LAURUSLABS',
 'laxmi organic industries ltd.': 'LXCHEM',
 'lemon tree hotels ltd.': 'LEMONTREE',
 'life insurance corporation of india': 'LICI',
 'linde india ltd.': 'LINDEINDIA',
 'lupin ltd.': 'LUPIN',
 'lux industries ltd.': 'LUXIND',
 'mmtc ltd.': 'MMTC',
 'mrf ltd.': 'MRF',
 'mtar technologies ltd.': 'MTARTECH',
 'macrotech developers ltd.': 'LODHA',
 'mahanagar gas ltd.': 'MGL',
 'mahindra & mahindra financial services ltd.': 'M&MFIN',
 'mahindra & mahindra ltd.': 'M&M',
 'mahindra holidays & resorts india ltd.': 'MHRIL',
 'mahindra lifespace developers ltd.': 'MAHLIFE',
 'manappuram finance ltd.': 'MANAPPURAM',
 'mangalore refinery & petrochemicals ltd.': 'MRPL',
 'mankind pharma ltd.': 'MANKIND',
 'marico ltd.': 'MARICO',
 'maruti suzuki india ltd.': 'MARUTI',
 'mastek ltd.': 'MASTEK',
 'max financial services ltd.': 'MFSL',
 'max healthcare institute ltd.': 'MAXHEALTH',
 'mazagoan dock shipbuilders ltd.': 'MAZDOCK',
 'medplus health services ltd.': 'MEDPLUS',
 'metro brands ltd.': 'METROBRAND',
 'metropolis healthcare ltd.': 'METROPOLIS',
 'minda corporation ltd.': 'MINDACORP',
 'minda industries ltd.': 'MINDAIND',
 'mindtree ltd.': 'MINDTREE',
 'mphasis ltd.': 'MPHASIS',
 'mrs. bectors food specialities ltd.': 'MRSBECTOR',
 'muthoot finance ltd.': 'MUTHOOTFIN',
 'narayana hrudayalaya ltd.': 'NH',
 'nbcc (india) ltd.': 'NBCC',
 'ncc ltd.': 'NCC',
 'nesco ltd.': 'NESCO',
 'nhpc ltd.': 'NHPC',
 'nlc india ltd.': 'NLCINDIA',
 'nocil ltd.': 'NOCIL',
 'nse academy ltd.': 'NSEACADEMY',
 'ntpc ltd.': 'NTPC',
 'navin fluorine international ltd.': 'NAVINFLUOR',
 'navkar corporation ltd.': 'NAVKARCORP',
 'network18 media & investments ltd.': 'NETWORK18',
 'new india assurance company ltd.': 'NIACL',
 'nippon life india asset management ltd.': 'NAM-INDIA',
 'niraj cement structurals ltd.': 'NIRAJ',
 'nitin spinners ltd.': 'NITINSPIN',
 'noida toll bridge company ltd.': 'NOIDATOLL',
 'nongu agro (india) ltd.': 'NONGU',
 'norbord industries ltd.': 'NORBORD',
 'nureca ltd.': 'NURECA',
 'oberoi realty ltd.': 'OBEROIRLTY',
 'oil & natural gas corporation ltd.': 'ONGC',
 'olectra greentech ltd.': 'OLECTRA',
 'omax autos ltd.': 'OMAXAUTO',
 'omaxe ltd.': 'OMAXE',
 'oracle financial services software ltd.': 'OFSS',
 'orange renewable power pvt ltd.': 'ORANGE',
 'orchid pharma ltd.': 'ORCHIDPHAR',
 'orissa minerals development company ltd.': 'ORISSAMINE',
 'orient cement ltd.': 'ORIENTCEM',
 'orient electric ltd.': 'ORIENTELEC',
 'orient paper & industries ltd.': 'ORIENTPPR',
 'oriental bank of commerce': 'ORIENTBANK',
 'pnb housing finance ltd.': 'PNBHOUSING',
 'pnc infratech ltd.': 'PNCINFRA',
 'pvr ltd.': 'PVR',
 'page industries ltd.': 'PAGEIND',
 'paisalo digital ltd.': 'PAISALO',
 'palladium hotels ltd.': 'PALLADIUM',
 'panyam cements & mineral industries ltd.': 'PANYAMCEM',
 'parag milk foods ltd.': 'PARAGMILK',
 'paras defence and space technologies ltd.': 'PARASDEF',
 'parekh aluminex ltd.': 'PAREKHPLAT',
 'pfizer ltd.': 'PFIZER',
 'phillips carbon black ltd.': 'PHILIPCARB',
 'phoenix mills ltd.': 'PHOENIXLTD',
 'pidilite industries ltd.': 'PIDILITIND',
 'piramal enterprises ltd.': 'PEL',
 'piramal glass ltd.': 'PIRAMALGL',
 'pitti engineering ltd.': 'PITTIENG',
 'pnc menon developers ltd.': 'SOBHA',
 'polycab india ltd.': 'POLYCAB',
 'polyplex corporation ltd.': 'POLYPLEX',
 'power finance corporation ltd.': 'PFC',
 'power grid corporation of india ltd.': 'POWERGRID',
 'precision wires india ltd.': 'PRECWIRE',
 'premier polyfilm ltd.': 'PREMIERPOL',
 'prestige estates projects ltd.': 'PRESTIGE',
 'prince pipes and fittings ltd.': 'PRINCEPIPE',
 'procter & gamble hygiene and health care ltd.': 'PGHH',
 'procter & gamble health ltd.': 'PGHL',
 'prozone intu properties ltd.': 'PROZONINTU',
 'punjab national bank': 'PNB',
 'punjab & sind bank': 'PSB',
 'quess corp ltd.': 'QUESS',
 'quick heal technologies ltd.': 'QUICKHEAL',
 'quess east bengal fc ltd.': 'QEBFC',
 'repl ltd.': 'REPL',
 'rpp infra projects ltd.': 'RPPINFRA',
 'rswm ltd.': 'RSWM',
 'radico khaitan ltd.': 'RADICO',
 'rail vikas nigam ltd.': 'RVNL',
 'rain industries ltd.': 'RAIN',
 'rajesh exports ltd.': 'RAJESHEXPO',
 'rallis india ltd.': 'RALLIS',
 'ramco cements ltd.': 'RAMCOCEM',
 'ratnamani metals & tubes ltd.': 'RATNAMANI',
 'raymond ltd.': 'RAYMOND',
 'redington (india) ltd.': 'REDINGTON',
 'relaxo footwears ltd.': 'RELAXO',
 'reliance industries ltd.': 'RELIANCE',
 'reliance power ltd.': 'RPOWER',
 'repco home finance ltd.': 'REPCOHOME',
 'route mobile ltd.': 'ROUTE',
 'ruchi soya industries ltd.': 'RUCHI',
 'rural electrification corporation ltd.': 'RECLTD',
 's chand and company ltd.': 'SCHAND',
 's h kelkar and company ltd.': 'SHK',
 's.a.l. steel ltd.': 'SALSTEEL',
 'sbi cards and payment services ltd.': 'SBICARD',
 'skf india ltd.': 'SKFINDIA',
 'srf ltd.': 'SRF',
 'sadbhav engineering ltd.': 'SADBHAV',
 'sagar cements ltd.': 'SAGCEM',
 'saksoft ltd.': 'SAKSOFT',
 'sakun engineers ltd.': 'SAKUN',
 'salasar techno engineering ltd.': 'SALASAR',
 'salona cotspin ltd.': 'SALONA',
 'salzer electronics ltd.': 'SALZERELEC',
 'samkrg pistons and rings ltd.': 'SAMKRG',
 'sanofi india ltd.': 'SANOFI',
 'sarda energy & minerals ltd.': 'SERML',
 'saregama india ltd.': 'SAREGAMA',
 'satin creditcare network ltd.': 'SATIN',
 'savita oil technologies ltd.': 'SAVITAOIL',
 'schaeffler india ltd.': 'SCHAEFFLER',
 'schneider electric infrastructure ltd.': 'SCHNEIDER',
 'seamec ltd.': 'SEAMECLTD',
 'security and intelligence services (india) ltd.': 'SIS',
 'sequent scientific ltd.': 'SEQUENT',
 'shalby ltd.': 'SHALBY',
 'shankara building products ltd.': 'SHANKARA',
 'sharda motor industries ltd.': 'SHARDAMOTR',
 'shemaroo entertainment ltd.': 'SHEMAROO',
 'shilpa medicare ltd.': 'SHILPAMED',
 'shoppers stop ltd.': 'SHOPERSTOP',
 'shree cement ltd.': 'SHREECEM',
 'shree pushkar chemicals & fertilisers ltd.': 'SHREEPUSHK',
 'shrenik ltd.': 'SHRENIK',
 'shriram city union finance ltd.': 'SHRIRAMCIT',
 'shriram transport finance co. ltd.': 'SRTRANSFIN',
 'siemens ltd.': 'SIEMENS',
 'signet industries ltd.': 'SIGNET',
 'simplex infrastructures ltd.': 'SIMPLEXINF',
 'sintex plastics technology ltd.': 'SPTL',
 'sintex industries ltd.': 'SINTEX',
 'sirca paints india ltd.': 'SIRCA',
 'siti networks ltd.': 'SITINET',
 'skipper ltd.': 'SKIPPER',
 'smartlink holdings ltd.': 'SMARTLINK',
 'smiths & founders (india) ltd.': 'SAFL',
 'sobha ltd.': 'SOBHA',
 'solar industries india ltd.': 'SOLARINDS',
 'somany home innovation ltd.': 'SHIL',
 'somany ceramics ltd.': 'SOMANYCERA',
 'sonata software ltd.': 'SONATSOFTW',
 'spandana sphoorty financial ltd.': 'SPANDANA',
 'speciality restaurants ltd.': 'SPECIALITY',
 "spencer's retail ltd.": 'SPRETAIL',
 'spicejet ltd.': 'SPICEJET',
 'star cement ltd.': 'STARCEMENT',
 'star paper mills ltd.': 'STARPAPER',
 'sterlite technologies ltd.': 'STLTECH',
 'strides pharma science ltd.': 'STAR',
 'subros ltd.': 'SUBROS',
 'sudarshan chemical industries ltd.': 'SUDARSCHEM',
 'sun pharma advanced research company ltd.': 'SPARC',
 'sun pharma ltd.': 'SUNPHARMA',
 'sun tv network ltd.': 'SUNTV',
 'sundaram finance ltd.': 'SUNDARMFIN',
 'sundram fasteners ltd.': 'SUNDRMFAST',
 'sunflag iron and steel company ltd.': 'SUNFLAG',
 'suprajit engineering ltd.': 'SUPRAJIT',
 'supreme industries ltd.': 'SUPREMEIND',
 'supreme petrochem ltd.': 'SUPPETRO',
 'suraksha realty ltd.': 'SURAKSHA',
 'surya roshni ltd.': 'SURYAROSNI',
 'sutlej textiles and industries ltd.': 'SUTLEJTEX',
 'suzlon energy ltd.': 'SUZLON',
 'swan energy ltd.': 'SWANENERGY',
 'swan industries ltd.': 'SWANINDS',
 'swastika investmart ltd.': 'SWASTIKA',
 'swelect energy systems ltd.': 'SWELECTES',
 'symphony ltd.': 'SYMPHONY',
 'syngene international ltd.': 'SYNGENE',
 'tafe ltd.': 'TAFE',
 'tci express ltd.': 'TCIEXP',
 'tcns clothing co. ltd.': 'TCNSBRANDS',
 'ttk healthcare ltd.': 'TTKHLTCARE',
 'tv today network ltd.': 'TVTODAY',
 'tvs motor company ltd.': 'TVSMOTOR',
 'talbros automotive components ltd.': 'TALBROAUTO',
 'tata chemicals ltd.': 'TATACHEM',
 'tata consumer products ltd.': 'TATACONSUM',
 'tata elxsi ltd.': 'TATAELXSI',
 'tata metaliks ltd.': 'TATAMETALI',
 'tata motors ltd.': 'TATAMOTORS',
 'tata power company ltd.': 'TATAPOWER',
 'tata steel ltd.': 'TATASTEEL',
 'tata teleservices (maharashtra) ltd.': 'TTML',
 'tata consultancy services ltd.': 'TCS',
 'tech mahindra ltd.': 'TECHM',
 'techno electric & engineering company ltd.': 'TECHNOE',
 'thangamayil jewellery ltd.': 'THANGAMAYL',
 'the indian hotels co. ltd.': 'INDHOTEL',
 'the new india assurance company ltd.': 'NIACL',
 'the ramco cements ltd.': 'RAMCOCEM',
 'thermax ltd.': 'THERMAX',
 'thomas cook (india) ltd.': 'THOMASCOOK',
 'thyrocare technologies ltd.': 'THYROCARE',
 'tide water oil co. (india) ltd.': 'TIDEWATER',
 'timken india ltd.': 'TIMKEN',
 'tips industries ltd.': 'TIPSINDLTD',
 'titan company ltd.': 'TITAN',
 'torrent pharmaceuticals ltd.': 'TORNTPHARM',
 'torrent power ltd.': 'TORNTPOWER',
 'total s.a.': 'TOTAL',
 'tourism finance corporation of india ltd.': 'TFCILTD',
 'trident ltd.': 'TRIDENT',
 'tube investments of india ltd.': 'TUBEINVEST',
 'tulip telecommunications ltd.': 'TTML',
 'tata starbucks ltd.': 'TATASTARBU',
 'u.s. polo assn.': 'USPA',
 'ufo moviez india ltd.': 'UFOMOVIES',
 'upl ltd.': 'UPL',
 'udaipur cement works ltd.': 'UDAIWD',
 'ultratech cement ltd.': 'ULTRACEMCO',
 'union bank of india': 'UNIONBANK',
 'united breweries ltd.': 'UBL',
 'united drilling tools ltd.': 'UNIDT',
 'united spirits ltd.': 'MCDOWELL-N',
 'united textiles ltd.': 'UNITEDTEX',
 'usha martin ltd.': 'USHAMART',
 'va tech wabag ltd.': 'WABAG',
 'vst industries ltd.': 'VSTIND',
 'vakrangee ltd.': 'VAKRANGEE',
 'vardhman special steels ltd.': 'VSSL',
 'vascon engineers ltd.': 'VASCON',
 'vaswani industries ltd.': 'VASWANI',
 'vedanta ltd.': 'VEDL',
 "venky's (india) ltd.": 'VENKEYS',
 'ventura textiles ltd.': 'VENTURA',
 'verkaat testing and certification ltd.': 'VERKAAT',
 'verus food & beverages ltd.': 'VERUSFOOD',
 'vesuvius india ltd.': 'VESUVIUS',
 'vibrant global capital ltd.': 'VIBRANT',
 'vidhi specialty food ingredients ltd.': 'VIDHIING',
 'vidli restaurants ltd.': 'VIDLI',
 'vijaya diagnostic centre ltd.': 'VIJAYA',
 'vikas ecotech ltd.': 'VIKASECO',
 'vikas lifecare ltd.': 'VIKASLIFE',
 'vikas multicorp ltd.': 'VIKASMCORP',
 'vinati organics ltd.': 'VINATIORGA',
 'vindhya telelinks ltd.': 'VINDHYATEL',
 'vintron informatics ltd.': 'VINTRON',
 'vinyl chemicals (india) ltd.': 'VINYLINDIA',
 'vipul ltd.': 'VIPULLTD',
 'vodafone idea ltd.': 'IDEA',
 'voltas ltd.': 'VOLTAS',
 'wabco india ltd.': 'WABCOINDIA',
 'welspun corp ltd.': 'WELCORP',
 'welspun enterprises ltd.': 'WELENT',
 'welspun india ltd.': 'WELSPUNIND',
 'west coast paper mills ltd.': 'WSTCSTPAPR',
 'westlife development ltd.': 'WESTLIFE',
 'whirlpool of india ltd.': 'WHIRLPOOL',
 'white organic agro ltd.': 'WOAL',
 'williamson magor & company ltd.': 'WILLAMAGOR',
 'wipro ltd.': 'WIPRO',
 'wonderla holidays ltd.': 'WONDERLA',
 'woods (india) ltd.': 'WOODSIND',
 'worthington industries ltd.': 'WORTH',
 'welspun investments and commercials ltd.': 'WELINV',
 'zandu realty ltd.': 'ZANDUREALT',
 'zee entertainment enterprises ltd.': 'ZEEL',
 'zensar technologies ltd.': 'ZENSARTECH',
 'zota health care ltd.': 'ZOTA',
 'avas': 'avasahe',
 'bharathi': 'bharatras',
 'laxmip': 'laxmipat',
 'laxmipat': 'laxmipatid',
 'niraj': 'nirajceme',
 'repl': 'repl',
 'titan': 'titan',
 'umang': 'umang',
 'us': 'uspa',
 'va': 'vaibhav',
 'voda': 'vodaphon',
 'wels': 'welspun',
 'west': 'westlife',
 'wipro': 'wipro'}

# Define the API key for the Telegram bot
API_KEY ="6508811818:AAHeAwqCEeZ8K5DL4bhQ9ktKu8L9euHrV6Q"

bot = telebot.TeleBot(API_KEY)

# Define the API keys for fetching news articles
API_KEYS = [
    'ef41b60f3790422bbf82ed26c3ebbbe2',  # API key 1
    '119ba1f1e2e649cd9d69d4042d31b50a',  # API key 2
    'a23932b08a21431e9eb6ca4e07c58b4c',  # API key 3
    '7171dd6466c045cbbdc88085e91fc22e',  # API key 4
    '4140a77ba7d4447b9983b3231d77ad8a',  # API key 5
    'fbc61f84df1248a9a6c12701f1912b53'   # API key 6
]

total_processing_time = []

# Function to analyze sentiment of news articles
def analyze_sentiment(articles):
    """Analyzes the sentiment of each news article using TextBlob."""
    sentiment_scores = []
    for article in articles:
        if isinstance(article, dict):
            title = article.get("title", "")  # Get the title or use an empty string if not available
            description = article.get("description", "")  # Get the description or use an empty string if not available

            # Check if both title and description are not None
            if title is not None and description is not None:
                text = title + " " + description

                blob = TextBlob(text)
                polarity = blob.sentiment.polarity
                subjectivity = blob.sentiment.subjectivity

                sentiment_scores.append((polarity, subjectivity))

    # Calculate means
    polarity_mean = np.mean([score[0] for score in sentiment_scores])
    subjectivity_mean = np.mean([score[1] for score in sentiment_scores])

    return polarity_mean, subjectivity_mean

def get_investment_recommendation(polarity, subjectivity):
    if polarity >= 0.25 and subjectivity <= 0.30:
        return "You may consider investing."
    elif 0.06 <= polarity <= 0.24 and subjectivity <= 0.40:
        return "You may consider investing, but it could be risky."
    else:
        return "It's not advisable to invest at the moment."

# Handler for '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Enter the stock name.")

# Handler for all messages
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    global StockName

    start_time = time.time()
    l = message.text.lower()  # Convert input to lowercase
    for key, value in nifty_500_dict.items():
        if l in key.lower():  # Check if the lowercase input is in lowercase key
            current_company = value
            StockName = key  # Set the stock name
            bot.reply_to(message, f"Stock name set to: {StockName}")
            break
    else:
        bot.reply_to(message, "Invalid stock name. Please try again.")
        return  # Exit the function if the stock name is invalid
    current_company = current_company + ".ns"

    current_date = datetime.date.today()
    start_date = current_date - datetime.timedelta(days=14)
    end_date = current_date

    # Download data
    data = yf.download(current_company, start=start_date, end=end_date)
    high = data['High']
    low = data['Low']

    # Calculate correlation coefficient
    covariance = np.sum([(high.iloc[i] - np.mean(high)) * (low.iloc[i] - np.mean(low)) for i in range(len(high))]) / len(high)
    standard_deviation_high = np.sqrt(np.sum([(high.iloc[i] - np.mean(high))**2 for i in range(len(high))]) / len(high))
    standard_deviation_low = np.sqrt(np.sum([(low.iloc[i] - np.mean(low))**2 for i in range(len(low))]) / len(low))
    correlation_coefficient = covariance / (standard_deviation_high * standard_deviation_low)

    # Calculate predicted high and low
    latest_high_price = data['High'].iloc[-1]
    mean_of_high_prices = data['High'].iloc[-14:].mean()
    latest_low_price = data['Low'].iloc[-1]
    mean_of_low_prices = data['Low'].iloc[-14:].mean()

    # Predict high and low
    High_predicted = correlation_coefficient * (latest_high_price - mean_of_high_prices) + mean_of_high_prices
    Low_predicted = correlation_coefficient * (latest_low_price - mean_of_low_prices) + mean_of_low_prices
    if Low_predicted > 1500:
        Low_predicted = Low_predicted + (Low_predicted * 0.010)
    if High_predicted > 1500:
        High_predicted = High_predicted + (High_predicted * 0.005)

    # Fetch news articles
    articles = fetch_news_articles(StockName)
    if articles is not None:
        extracted_articles = []
        for article in articles["articles"]:
            extracted_article = {
                "title": article["title"],
                "description": article["description"]
            }
            extracted_articles.append(extracted_article)

        polarity_mean, subjectivity_mean = analyze_sentiment(extracted_articles)
        recommendation = get_investment_recommendation(polarity_mean, subjectivity_mean)

        print(f"Polarity Mean: {polarity_mean}\nSubjectivity Mean: {subjectivity_mean}")

        end_time = time.time()  # Record the end time
        processing_time = end_time - start_time
        total_processing_time.append(processing_time)
        bot.reply_to(message, f"\nRecommendation: {recommendation}\nHigh: {round(High_predicted, 2)}\nLow: {round(Low_predicted, 2)}\n\nProcessing Time: {processing_time}")
    else:
        bot.reply_to(message, "Failed to fetch news articles. Please try again later.")

def fetch_news_articles(stock_name):
    for api_key in API_KEYS:
        try:
            api = NewsApiClient(api_key=api_key)
            articles = api.get_everything(q=stock_name)
            if articles['totalResults'] > 0:
                return articles
        except:
            continue
    return None

# Start the bot
print("Hey, I am up....")
bot.polling()
