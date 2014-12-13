# paste this into your .bash_profile on fish.arsc.edu

module swap PrgEnv-pgi PrgEnv-gnu
# netcdf-hdf5parallel/4.2.0 requires GCC 4.7
module swap gcc/4.9.0 gcc/4.7.1

for module in \
    fftw/3.3.4.0 \
    petsc/3.3.00 \
    netcdf-hdf5parallel/4.2.0 \
    gsl/1.15.gnu;
do
    module load $module
done

# petsc/3.3.00 does not work with the default tpsl
module swap tpsl/1.2.00 tpsl/1.3.00
