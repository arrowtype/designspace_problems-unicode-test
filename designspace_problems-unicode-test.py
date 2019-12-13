from pprint import pprint
from designspaceProblems import DesignSpaceChecker
import ufoProcessor
from ufoProcessor import DesignSpaceProcessor, getUFOVersion, getLayer, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor
from fontParts.fontshell import RFont

dc = DesignSpaceChecker("unicodes-test-project/Unicodes Test.designspace")
dc.checkEverything()

# now all problems are stored in dc.problems
pprint(dc.problems)