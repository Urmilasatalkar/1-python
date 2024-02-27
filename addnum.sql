create or replace function add_num(p1 number,p2 number)
return number
is
begin
commit;
	if p1 is null then
		
		return p2;
	elsif p2 is null then
		return p1;
	else
		return(p1+p2);
	end if;
end;
/