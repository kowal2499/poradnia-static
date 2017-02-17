<?php
    // build the imgs array
    $imgs = Array();
    $counter = 0;
    foreach (array_diff(scandir('img'), array('..', '.')) as $file) {
        if (strtolower(pathinfo($file, PATHINFO_EXTENSION)) === 'jpg') {
            
            $thumbnail = '';

            if (file_exists('img/thumbs/' . $file)) {
                $thumbnail = 'img/thumbs/' . $file;
            } else {
                $thumbnail = $file;
            }
            
            $record = array('id' => $counter, 'fullPath'=> 'img/' . $file, 
                                'file' => $file, 'thumbnail' => $thumbnail);
            array_push($imgs, $record);
            $counter++;
        }
    }

    echo json_encode( $imgs );

?>