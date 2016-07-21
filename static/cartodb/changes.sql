SELECT distinct on (meetpunt) *, round((ec/1000)::numeric,2) as ecms,
to_char(ec_toename/1000, 'S90.00') as ecdelta,
to_char(datum,'TMDy DD TMMon YYYY') as datestr
FROM allemetingen 
where wndid > 1 and datum > '01-01-2015'
order by meetpunt,datum desc