function add_line_to_lightdm_file(){
    local file_path_and_name;
    local string_to_add_line_after;
    local line_to_add;

    file_path_and_name="/etc/lightdm/lightdm.conf";
    string_to_add_line_after_in_regex="\[SeatDefaults\]";
    line_to_add="xserver-command=X -s 0 -dpms";
    
    sed -i -e "/$string_to_add_line_after_in_regex$/a$line_to_add" $file_path_and_name;    
}

add_line_to_lightdm_file
