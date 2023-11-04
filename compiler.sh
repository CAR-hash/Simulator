for i in {0..99}
do
        pip-compile ./hdl_${i}/requirements.in
done