export me=$(whoami)

myjobs()
{
    echo "Jobs for $me"
    squeue --me
}

nodes()
{
    case "$1" in
        "")
        # Let's assume help in required.
        cat - <<EOF
The nodes command allows you to get information about the
nodes in the cluster. The syntax is:

    nodes {what-you-want-to-know-about}

The options are:

    free    -- show the idle nodes available for assignment.
    avail   -- same as free
    info    -- a more nicely formatted output from <sinfo>
    queues  -- a more nicely formatted output from <squeue>

EOF
        ;;
 
        free|avail)
        sinfo | grep "idle"
        ;;

        info)
        sinfo -o "%20P %5D %14F %8z %10m %10d %11l %16f %N"
        ;;

        queues)
        squeue -o "%8i %12j %4t %10u %20q %20a %10g %20P %10Q %5D %11l %11L %R"
        ;;

    esac
}

submit()
{
    case "$1" in
        "")
        # Help out the user.
        cat - <<EOF
The submit command allows you to submit slurm jobs in
batch mode (the usual way of doing things). You can provide
the name of your job with or without the ".slurm" on the end
of the file name. You can also submit multiple jobs at the
same time. Here are some examples:

    submit myjob.slurm -- tells slurm to run myjob.slurm
    submit myjob  -- tells slurm to run myjob.slurm
    submit myjob* -- tells slurm to run any slurm jobs whose
        names start with "myjob"

Assuming something has been submitted, you will see your running
jobs summarized at the end of the command.
EOF
    return
    ;;
    esac

    script="$1"
    candidates=$(ls -1 $script)    
    if [ -z $candidates ]; then
        candidates=$(ls -1 $script.slurm)
    fi
    if [ -z $candidates ]; then 
        submit
        return
    fi

    for f in $candidates; do 
        echo "Submitting batch job $f"
        myname=`basename $f`
        sbatch -J $myname --parsable "$f"
    done;
    myjobs
}
