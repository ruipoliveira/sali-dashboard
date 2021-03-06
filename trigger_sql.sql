﻿CREATE OR REPLACE FUNCTION alarm_occurred() returns trigger as $alarm$ 
DECLARE
varmax FLOAT;
varmin FLOAT;
BEGIN

varmax := (select max from saliapp_alarmssettings where id_sensor_id= new.id_sensor_id);
varmin := (select min from saliapp_alarmssettings where id_sensor_id= new.id_sensor_id);

IF (new.value >= varmax) THEN 
	insert into saliapp_alarms (id_reading_id, checked, max_or_min) VALUES (new.id, 'f', 't');
	return new;
END IF;
IF (new.value <= varmin) THEN 
	insert into saliapp_alarms (id_reading_id, checked, max_or_min) VALUES (new.id, 'f', 'f');
	return new;
END IF;

RETURN NULL;
END
$alarm$
LANGUAGE plpgsql;

create trigger trigger_alarm_occurred after insert on saliapp_reading
for each row execute procedure alarm_occurred(); 

DROP FUNCTION alarm_occurred(); 

DROP TRIGGER trigger_alarm_occurred ON saliapp_reading;

