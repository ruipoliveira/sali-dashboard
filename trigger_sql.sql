



CREATE FUNCTION emp_stamp() RETURNS trigger AS $emp_stamp$
    BEGIN
    	INSERT INTO films VALUES
    	(90);
    END;
$emp_stamp$ LANGUAGE plpgsql;


CREATE TRIGGER emp_stamp BEFORE INSERT ON emp
    FOR EACH ROW EXECUTE PROCEDURE emp_stamp();

