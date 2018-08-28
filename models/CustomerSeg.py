import uuid
from cassandra.cqlengine import columns
from models.base import Base

class CustomerSeg(Base):
	party_id = columns.Text(primary_key=True)
	fresco13_mseg = columns.Text()
	fresco13_seg = columns.Text(index=True)
	fresco13_sseg = columns.Text()
	#match_flag = columns.Text()

	def get_data(self):
		return {
			'party_id': str(self.party_id),
			'fresco_mseg': str(self.fresco13_mseg),
			'fresco_seg': str(self.fresco13_seg),
			'fresco_sseg': str(self.fresco13_sseg),
			#'match_flag': str(self.match_flag)
		}
		
class SegmentLookup(Base):
	segment_cd = columns.Text(primary_key=True)
	segment = columns.Text()
	

	def get_data_segment(self):
		return {
			'segment_cd': str(self.segment_cd),
			'segment': str(self.segment_cd)
		}		